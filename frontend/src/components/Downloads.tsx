import { useNavigate, useSearchParams } from "react-router-dom";
import { useEffect, useState, type ChangeEvent } from "react";
import {
  Button,
  ButtonGroup,
  Checkbox,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeadCell,
  TableRow,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Label,
  TextInput,
} from "flowbite-react";
import type { TransmissionTorrent } from "../types/TransmissionTorrent";
import { TorrentStatus } from "../types/TorrentStatus";
import { HiMiniStop, HiMiniPlay, HiMiniTrash } from "react-icons/hi2";
import type { NcoreTorrent } from "../types/ncore-torrent.interface";
import { formatSize } from "../utils/format";

const Downloads = () => {
  const navigate = useNavigate();

  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [torrents, setTorrents] = useState<TransmissionTorrent[]>([]);
  const [selectedTorrents, setSelectedTorrents] = useState<Set<string>>(
    new Set()
  );

  const [searchParams] = useSearchParams();
  const downloadUrl = searchParams.get("url");
  const tmdbId = searchParams.get("tmdbid");

  const [showModal, setShowModal] = useState(false);
  const [modalLoading, setModalLoading] = useState(false);
  const [newTorrent, setNewTorrent] = useState<NcoreTorrent | null>(null);

  const getTorrentList = async (): Promise<
    { fields: TransmissionTorrent }[]
  > => {
    const url = new URL(`/torrents/`, import.meta.env.VITE_BACKEND_URL);
    const response = await fetch(url, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) {
      throw new Error(`Error fetching torrents ${response.text()}`);
    }

    return response.json();
  };

  useEffect(() => {
    const fetchTorrents = async () => {
      updateTorrents();
    };
    fetchTorrents();
  }, []);

  useEffect(() => {
    if (downloadUrl && tmdbId) {
      setShowModal(true);
    }
  }, [downloadUrl, tmdbId]);

  useEffect(() => {
  if (!downloadUrl || !tmdbId) {
    setShowModal(false);
    setNewTorrent(null);
    setModalLoading(false);
  }
}, [downloadUrl, tmdbId]);

  useEffect(() => {
    const getDetailsFromTracker = async () => {
      setModalLoading(true);
      if (downloadUrl) {
        const ncoreId = new URL(downloadUrl).searchParams.get("id");
        const url = new URL(
          `/tracker/${ncoreId}`,
          import.meta.env.VITE_BACKEND_URL
        );
        const response = await fetch(url, {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        });
        if (!response.ok) {
          throw new Error(
            `An error occured. cannot get new torrent details from tracker.` +
              ` ${response.status}: ${response.text()}`
          );
        }
        const data = await response.json();
        setNewTorrent(data);
        setModalLoading(false);
      }
    };
    getDetailsFromTracker();
  }, [downloadUrl]);

  function selectTorrent(event: ChangeEvent<HTMLInputElement>) {
    const torrentId = event.target.id;
    if (!torrentId)
      throw new Error("Error when selecting torrent. No hash ID found!");
    const newSet = new Set(selectedTorrents);
    if (event.target.checked) {
      newSet.add(torrentId);
    } else {
      newSet.delete(torrentId);
    }
    setSelectedTorrents(newSet);
  }

  async function updateTorrents() {
    setIsLoading(true);
    setErrorMessage(null);
    try {
      const data: { fields: TransmissionTorrent }[] = await getTorrentList();
      setTorrents(data.map((t) => t.fields));
    } catch (error) {
      const exception = error as { error: string };
      setErrorMessage(exception.error);
    } finally {
      setIsLoading(false);
    }
  }

  const stopTorrents = async () => {
    const url = new URL(`/torrents/stop`, import.meta.env.VITE_BACKEND_URL);
    const selectedTorrentIds = Array.from(selectedTorrents);
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ids: selectedTorrentIds,
      }),
    });
    if (!response.ok) {
      throw new Error("Error when tried to pause torrent.");
    }

    /**
     * TODO
     * Implement polling, because sometimes
     * the update happens too fast
     * and torrent client (transmission)
     * didn't stop the torrent at time of update
     * so the status is still shows the prev state.
     */
    setSelectedTorrents(new Set());
    updateTorrents();
  };

  const startTorrents = async () => {
    const url = new URL(`/torrents/start`, import.meta.env.VITE_BACKEND_URL);
    const selectedTorrentIds = Array.from(selectedTorrents);
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ids: selectedTorrentIds }),
    });
    if (!response.ok) {
      throw new Error(
        `Error when tried to start torrents: ${selectedTorrentIds}`
      );
    }

    setSelectedTorrents(new Set());
    const updatedTorrentList = await getTorrentList();
    setTorrents(updatedTorrentList.map((t) => t.fields));
  };

  const deleteTorrents = async () => {
    const url = new URL(`/torrents/`, import.meta.env.VITE_BACKEND_URL);
    const selectedTorrentIds = Array.from(selectedTorrents);

    await fetch(url, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ids: selectedTorrentIds }),
    });

    setSelectedTorrents(new Set());
    updateTorrents();
  };

  const addNewTorrent = async () => {
    const url = new URL(`/torrents/download`, import.meta.env.VITE_BACKEND_URL);
    if(!(downloadUrl && tmdbId)) throw new Error("downloadUrl and tmdbId must be provided");
    
    await fetch(url, {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({url: downloadUrl, tmdbId: tmdbId})
    });
    
    navigate(location.pathname, {replace: true});
    setModalLoading(false);
    setShowModal(false);
    updateTorrents();
  };

  return (
    <>
      {isLoading ? (
        <div className="flex justify-center items-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : errorMessage ? (
        <div className="text-red-500 my-4 text-center">{errorMessage}</div>
      ) : (
        <div className="pt-8 bg-gray-700">
          <ButtonGroup>
            <Button
              color="alternative"
              disabled={selectedTorrents.size == 0}
              onClick={startTorrents}
            >
              <HiMiniPlay className="me-2 h-4 w-4" />
              Start
            </Button>
            <Button
              color="alternative"
              disabled={selectedTorrents.size == 0}
              onClick={stopTorrents}
            >
              <HiMiniStop className="me-2 h-4 w-4" />
              Stop
            </Button>
            <Button
              color="alternative"
              disabled={selectedTorrents.size == 0}
              onClick={deleteTorrents}
            >
              <HiMiniTrash className="me-2 h-4 w-4" />
              Remove &nbsp; <span>({selectedTorrents.size})</span>
            </Button>
          </ButtonGroup>
          <Table hoverable striped>
            <TableHead>
              <TableRow>
                <TableHeadCell className="p-4 rounded-none">
                  <Checkbox
                    onChange={(e) => {
                      if (e.target.checked) {
                        setSelectedTorrents(
                          new Set(torrents.map((t) => t.hashString))
                        );
                      } else {
                        setSelectedTorrents(new Set());
                      }
                    }}
                  />
                </TableHeadCell>
                <TableHeadCell>Name</TableHeadCell>
                <TableHeadCell>Status</TableHeadCell>
                <TableHeadCell>Progress</TableHeadCell>
                <TableHeadCell>Size</TableHeadCell>
              </TableRow>
            </TableHead>
            <TableBody className="divide-y">
              {torrents.map((torrent) => (
                <TableRow
                  key={torrent.id}
                  className="bg-white dark:border-gray-700 dark:bg-gray-800"
                >
                  <TableCell className="p-4">
                    <Checkbox
                      checked={selectedTorrents.has(torrent.hashString)}
                      onChange={(event) => selectTorrent(event)}
                      id={torrent.hashString}
                    />
                  </TableCell>
                  <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                    {torrent.name}
                  </TableCell>
                  <TableCell>{TorrentStatus[torrent.status]}</TableCell>
                  <TableCell>{(torrent.percentDone * 100).toFixed(0)} %</TableCell>
                  <TableCell>{formatSize(torrent.totalSize)}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>

          <Modal
            show={showModal}
            popup
            position="top-center"
            onClose={() => setShowModal(false)}
          >
            <ModalHeader>Add new torrent</ModalHeader>
            <ModalBody>
              {modalLoading ? (
                <div className="flex justify-center items-center py-8">
                  <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
                </div>
              ) : (
                <div className="space-y-8">
                  <div>
                    <div className="mb-2 block">
                      <Label htmlFor="torrentname">Name</Label>
                    </div>
                    <TextInput
                      type="text"
                      readOnly
                      disabled
                      id="torrentname"
                      value={newTorrent?.title}
                    />
                    <div className="flex gap-4">
                      <div className="flex-1">
                        <div>
                          <Label htmlFor="size">Size</Label>
                        </div>
                        <TextInput
                          type="text"
                          readOnly
                          disabled
                          id="size"
                          value={newTorrent?.size ? formatSize(newTorrent?.size._size) : "ERROR!"}
                        />
                      </div>
                      <div className="flex-1">
                        <div>
                          <Label htmlFor="size">Type</Label>
                        </div>
                        <TextInput
                          type="text"
                          readOnly
                          disabled
                          id="size"
                          value={newTorrent?.type}
                        />
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </ModalBody>
            <ModalFooter>
              <Button onClick={addNewTorrent} disabled={!(downloadUrl && tmdbId)}>Add</Button>
              <Button color="alternative" onClick={() => setShowModal(false)}>
                Cancel
              </Button>
            </ModalFooter>
          </Modal>
        </div>
      )}
    </>
  );
};

export default Downloads;