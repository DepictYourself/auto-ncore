export const formatSize = (bytes: number): string => {
  if (bytes >= 1024 ** 3) {
    return (bytes / 1024 ** 3).toFixed(2) + " GiB";
  } else if (bytes >= 1024 ** 2) {
    return (bytes / 1024 ** 2).toFixed(2) + " MiB";
  } else if (bytes >= 1024) {
    return (bytes / 1024).toFixed(2) + " KiB";
  } else {
    return bytes + " B";
  }
}