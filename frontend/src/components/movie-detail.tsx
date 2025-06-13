import { useLocation, useParams } from "react-router-dom";

const MovieDetail = () => {
  const { id } = useParams();
  const location = useLocation();
  const movie = location.state?.movie;
  if(!movie){
    return <p>Loading or fetching fallback data.</p>
  }
    
  return (
    <>
      <div>MovieDetail {movie.id}</div>
      <p>param id: {id}</p>
    </>
  );
};

export default MovieDetail;
