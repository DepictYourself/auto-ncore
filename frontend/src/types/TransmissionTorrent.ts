interface TransmissionTorrent {
  /**
   * you can extend this interface
   * there is more data available.
   * Don't forget to update the backend too!
   */
  id: number;
  hashString: string;
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