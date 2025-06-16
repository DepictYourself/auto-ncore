export enum TorrentStatus {
  Stopped = 0,
  QueuedToCheck = 1,
  Checking = 2,
  QueuedToDownload = 3,
  Downloading = 4,
  QueuedToSeed = 5,
  Seeding = 6
}