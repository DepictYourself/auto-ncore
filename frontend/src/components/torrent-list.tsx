import {
  Button,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeadCell,
  TableRow,
} from "flowbite-react";
import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import type { NcoreTorrent } from "../types/ncore-torrent.interface";
import { formatSize } from "../utils/format";

interface TorrentListProps {
  torrentSearchKeyword: string;
  tmdbId: string;
}

const TorrentList: React.FC<TorrentListProps> = ({
  torrentSearchKeyword,
  tmdbId,
}) => {
  const [torrentList, setTorrentList] = useState<NcoreTorrent[]>([]);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const searchTorrents = async (
    searchTerm: string
  ): Promise<NcoreTorrent[]> => {
    const url = new URL(
      `tracker/search/${encodeURIComponent(searchTerm)}`,
      import.meta.env.VITE_BACKEND_URL
    );
    console.log("searchTorrents() url: ", url);
    const response = await fetch(url);
    const data = await response.json();
    if (!response.ok || data.error) {
      throw new Error(data.error || "Unknown error occured.");
    }
    return data;
  };

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      setErrorMessage("");
      try {
        const data = await searchTorrents(torrentSearchKeyword);
        console.log("searchTorrent returned data: ", data);
        setTorrentList(data);
      } catch (e) {
        console.error(e);
        const errorMessage = `Torrent fetch error: ${e}`;
        setErrorMessage(errorMessage);
      } finally {
        setIsLoading(false);
      }
    };
    fetchData();
  }, [torrentSearchKeyword]);

  return (
    <>
      {isLoading ? (
        <div className="flex justify-center items-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
        </div>
      ) : errorMessage ? (
        <div className="text-red-500 my-4 text-center">{errorMessage}</div>
      ) : (
        <Table hoverable>
          <TableHead>
            <TableRow>
              <TableHeadCell>Title</TableHeadCell>
              <TableHeadCell>Size</TableHeadCell>
              <TableHeadCell>Type</TableHeadCell>
              <TableHeadCell>Upload date</TableHeadCell>
              <TableHeadCell>Seeders</TableHeadCell>
              <TableHeadCell>Leeches</TableHeadCell>
              <TableHeadCell>
                <span className="sr-only">Download</span>
              </TableHeadCell>
            </TableRow>
          </TableHead>
          <TableBody className="divide-y">
            {torrentList.map((torrent: NcoreTorrent) => (
              <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
                <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {torrent.title}
                </TableCell>
                <TableCell>{formatSize(torrent.size._size)}</TableCell>
                <TableCell>{torrent.type}</TableCell>
                <TableCell>{torrent.date.split("T")[0]}</TableCell>
                <TableCell>{torrent.seed}</TableCell>
                <TableCell>{torrent.leech}</TableCell>
                {/* TODO */}
                <TableCell>
                  <Link
                    to={`/downloads?url=${encodeURIComponent(torrent.download)}
                    &tmdbid=${tmdbId}`}
                  >
                    <Button className="cursor-pointer" color="light">
                      Download
                    </Button>
                  </Link>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      )}
    </>
  );
};

export default TorrentList;
