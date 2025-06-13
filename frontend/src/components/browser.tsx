import Strip from './strip';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

const discoverTmdbMovies = async () => {
    const response = await fetch(BACKEND_URL + `/movie/discover`);
    if(!response.ok) throw new Error("Failed to fetch tmdb movies");
    return await response.json()
}

const browser = () => {
  return (
    <Strip title="Recent Movies" fetchFn={discoverTmdbMovies}/>
  )
}

export default browser