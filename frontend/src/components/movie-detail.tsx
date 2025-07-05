import { useLocation } from "react-router-dom";
import tmdbGenres from "../data/tmdbmoviegenres.json";
import { Badge } from "flowbite-react";
import TorrentList from "./torrent-list";
import type TmdbMovieInterface from "../types/tmdb-movie.interface";

const MovieDetail = () => {
  //const { id } = useParams();
  const location = useLocation();
  const movie: TmdbMovieInterface = location.state?.movie;
  if (!movie) {
    return <p>Loading or fetching fallback data.</p>;
    // TODO
    // Implement fetching fallback data using id.
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
      <div
        className="relative w-full h-[500px] mb-16 bg-cover bg-center"
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

      <TorrentList torrentSearchKeyword={movie.original_title} tmdbId={movie.id} />
    </>
  );
};

export default MovieDetail;
