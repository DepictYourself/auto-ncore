import { useEffect, useState } from "react";
import { Card } from "flowbite-react";

type Media = {
    id: string;
    adult: boolean;
    poster_path: string;
    backdrop_path: string;
    genre_ids: number[];
    title: string;
    original_title: string;
    overview: string;
    popularity: number;
    release_date: string;
    video: boolean;
    vote_average: number;
    vote_count: number;
};

type StripProps = {
    title?: string;
    fetchFn: () => Promise<Media[] | undefined>;
};

const Strip: React.FC<StripProps> = ({ title, fetchFn }) => {
    const [list, setList] = useState<Media[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

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
            {title && <h2 className="text-xl font-semibold mb-2">{title}</h2>}
            <div className="overflow-x-auto whitespace-nowrap">
                <div className="flex gap-4">
                    {list.map((item) => (
                        <Card
                            key={item.id}
                            className="min-w-[150px] w-36 flex-shrink-0"
                        >
                            <img
                                src={`https://image.tmdb.org/t/p/w300/${item.poster_path}`} 
                                alt={`${item.title} poster`}
                                className="w-full h-48 object-cover rounded-t-lg" 
                            />
                            <div className="p-2 text-sm text-center">{item.title}</div>
                        </Card>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Strip;
