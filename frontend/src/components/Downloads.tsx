import { useSearchParams } from "react-router-dom";
import Navbar from "./navbar";
import { useEffect, useState } from "react";
import {
  Checkbox,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeadCell,
  TableRow,
} from "flowbite-react";
import type { TransmissionTorrent } from "../types/TransmissionTorrent";
import { TorrentStatus } from "../types/TorrentStatus";

const Downloads = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [torrents, setTorrents] = useState<TransmissionTorrent[]>([]);
  const [searchParams] = useSearchParams();
  const downloadUrl = searchParams.get("url");

  const getTorrentList = async () => {
    const url = new URL(`/torrents`, import.meta.env.VITE_BACKEND_URL);
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
      setIsLoading(true);
      setErrorMessage(null);
      try {
        const data: {fields: TransmissionTorrent}[] = await getTorrentList();
        console.log("Downloads component getTorrentList data: ", data);
        setTorrents(data.map(t => t.fields));
      } catch (error) {
        const exception = error as { error: string };
        setErrorMessage(exception.error);
      } finally {
        setIsLoading(false);
      }
    };
    fetchTorrents();
  }, []);

  return (
    <>
      <Navbar />

      {downloadUrl ?? <p>{downloadUrl}</p>}

      {isLoading ? (
        <div className="flex justify-center items-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : errorMessage ? (
        <div className="text-red-500 my-4 text-center">{errorMessage}</div>
      ) : (
        <Table hoverable striped>
          <TableHead>
            <TableRow>
              <TableHeadCell className="p-4">
                <Checkbox />
              </TableHeadCell>
              <TableHeadCell>Name</TableHeadCell>
              <TableHeadCell>Status</TableHeadCell>
              <TableHeadCell>Progress</TableHeadCell>
              <TableHeadCell>Size</TableHeadCell>
            </TableRow>
          </TableHead>
          <TableBody className="divide-y">
            {torrents.map((torrent) => (
              <TableRow key={torrent.id} className="bg-white dark:border-gray-700 dark:bg-gray-800">
                <TableCell className="p-4">
                  <Checkbox />
                </TableCell>
                <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {torrent.name}
                </TableCell>
                <TableCell>{TorrentStatus[torrent.status]}</TableCell>
                <TableCell>{torrent.percentDone} %</TableCell>
                <TableCell>{torrent.totalSize}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      )}
      
    </>
  );
};

export default Downloads;
