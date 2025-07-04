import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import type TmdbMovieInterface from "../types/tmdb-movie.interface";
import type { TmdbTvShowInterface } from "../types/tmdb-tvshow.interface";

type StripProps = {
    title?: string;
    fetchFn: () => Promise<TmdbMovieInterface[] | undefined>;
};

const Strip: React.FC<StripProps> = ({ title, fetchFn }) => {
    const [list, setList] = useState<TmdbMovieInterface[] | TmdbTvShowInterface[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const isMovie = (item: TmdbMovieInterface | TmdbTvShowInterface):item is TmdbMovieInterface => {
      return (item as TmdbMovieInterface).title !== undefined;
    }

    const getDisplayName = (item: TmdbMovieInterface | TmdbTvShowInterface) => {
      return isMovie(item) ? item.title : item.name;
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await fetchFn();
                if(result){
                    setList(result);
                }
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            } catch (error: any) {
                setError(error.message || "Failed to load data");
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [fetchFn])
    
    if (loading) return <div className="p-4">Loading {title}...</div>;
    if (error) return <div className="p-4 text-red-500">Error loading {title}: {error}</div>;

    return (
        <div className="py-4 px-2">
            {title && <h2 className="text-xl font-bold mb-2">{title}</h2>}
            <div className="overflow-x-auto whitespace-nowrap px-2">
                <div className="flex gap-4 py-6">

                    {list.map((item) => (
                        <div
                            key={item.id}
                            className="flex bg-white dark:border-gray-800 shadow-lg flex-col 
                            w-48 sm:w-52 flex-shrink-0 rounded-lg overflow-hidden"
                        >
                            <Link to={`/movie/${item.id}`} state={{movie: item}}>
                                <img 
                                    src={`${import.meta.env.VITE_TMDB_IMG_URL}/w300${item.poster_path}`}
                                    alt={getDisplayName(item)}
                                    className="object-cover w-full h-72"
                                />
                                <div className="p-4 hidden sm:block">
                                    <h5 className="mb-1 text-xl font-semibold tracking-tight text-gray-900 ">
                                        {getDisplayName(item)}
                                    </h5>
                                    <div className="flex items-center">
                                        <svg 
                                            xmlns="http://www.w3.org/2000/svg" 
                                            className="w-5 h-5 text-amber-300"
                                            aria-hidden="true"
                                            fill="currentColor"
                                            viewBox="0 0 20 20"
                                        >
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                                        </svg>
                                        <span className="text-base text-gray-800 dark:text-gray-400">{item.vote_average.toFixed(1)}</span>
                                    </div>
                                    <p className="font-normal text-shadow-gray-800 dark:text-gray-400 line-clamp-3 max-h-32">
                                        {item.overview}
                                    </p>
                                </div>
                            </Link>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Strip;

