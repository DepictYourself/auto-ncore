interface TransmissionTorrent {
  id: number;
  name: string;
  percentDone: number;
  status: number;
  downloadDir: string;
  totalSize: number;
  downloadEver: number;
  uploadRation: number;
  magnetLink?: string;
}

export type { TransmissionTorrent };