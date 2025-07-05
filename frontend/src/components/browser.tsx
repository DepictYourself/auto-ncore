import type TmdbMovieInterface from '../types/tmdb-movie.interface';
import type { TmdbTvShowInterface } from '../types/tmdb-tvshow.interface';
import Strip from './strip';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

const discoverTmdbMovies = async (): Promise<TmdbMovieInterface[]> => {
    const response = await fetch(BACKEND_URL + `/movie/discover`);
    if(!response.ok) throw new Error("Failed to fetch tmdb movies");
    return await response.json()
}

const discoverTmdbTvShows = async (): Promise<TmdbTvShowInterface[]> => {
  const response = await fetch(BACKEND_URL + `/tvshow/discover`);
  if(!response.ok) throw new Error("Failed to fetch tmdb tv shows");
  return await response.json();

}

const browser = () => {
  return (
    <>
      <Strip title="Recent Movies" fetchFn={discoverTmdbMovies}/>
      <Strip title="Most popular Tv Shows" fetchFn={discoverTmdbTvShows} />
    </>
  )
}

export default browser