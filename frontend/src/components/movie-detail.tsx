/* eslint-disable @typescript-eslint/no-unused-vars */
import { Link, useLocation, useParams } from "react-router-dom";
import tmdbGenres from "../data/tmdbgenre.json";
import { Badge } from "flowbite-react";
import Navbar from "./navbar";
import TorrentList from "./torrent-list";

const MovieDetail = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { id } = useParams();
  const location = useLocation();
  const movie = location.state?.movie;
  if (!movie) {
    return <p>Loading or fetching fallback data.</p>;
  }

  const getMovieGenreList = (genreIdArr: number[]) => {
    const outputGenreNameArr: string[] = [];
    genreIdArr.forEach((id: number) => {
      const matchGenreObj = tmdbGenres["genres"].find((obj) => obj.id === id);
      if (matchGenreObj) {
        outputGenreNameArr.push(matchGenreObj?.name);
      }
    });
    return outputGenreNameArr;
  };

  return (
    <>
      <Navbar />

      <div
        className="relative w-full h-[500px] bg-cover bg-center"
        style={{
          backgroundImage: `linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(255,255,255,1)), url(${import.meta.env.VITE_TMDB_IMG_URL}/w1280${movie.backdrop_path})`
        }}
      >
        <div className="absolute bottom-8 left-8">
          <h1 className="text-4xl font-bold mb-4">{movie.title}</h1>
          
          {/* Genres */}
          <div className="flex flex-wrap gap-2">
            {
              getMovieGenreList(movie.genre_ids).map((genre: string) => (
                <Badge key={genre} color="gray">{genre}</Badge>
              ))
            }
          </div>
          <p className="text-lg max-w-5xl mt-4">{movie.overview}</p>
          <p className="mt-2 text-md">TMDB Rating: {movie.vote_average.toFixed(1)} ⭐</p>
        </div>
      </div>

      <TorrentList torrentSearchKeyword={movie.original_title} />
    </>
  );
};

export default MovieDetail;
