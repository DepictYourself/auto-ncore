export interface NcoreTorrent {
  id: string;
  title: string;
  key: string;
  size: {
    _unit: string;
    _size: number;
  }
  type: string;
  /**
   * @example: "2016-02-07T17:13:08"
   */
  date: string;
  seed: string;
  leech: string;
  download: string;
  url: string;
}