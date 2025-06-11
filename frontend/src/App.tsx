import {  } from 'react';
import './App.css'
import Navbar from './components/navbar';
import Strip from './components/strip';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

const discoverTmdbMovies = async () => {
    const response = await fetch(BACKEND_URL + `/movie/discover`);
    if(!response.ok) throw new Error("Failed to fetch tmdb movies");
    return await response.json()
}

function App() {
  return (
    <>
      <Navbar />
      <Strip title="Recent Movies" fetchFn={discoverTmdbMovies}/>
    </>
  )
}

export default App
