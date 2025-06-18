export default interface TmdbMovieInterface {
  adult: boolean;

  /**
   * @example: /uIpJPDNFoeX0TVml9smPrs9KUVx.jpg
   */
  backdrop_path: string;

  /**
   * @example: [ 27, 9648 ]
   */
  genre_ids: number[];

  /**
   * @example: 574475
   */
  id: string;
  
  /**
   * @example: "en"
   */
  original_language: string;


  original_title: string;

  overview: string;
  /**
   * @example: 1160.8402
   */
  popularity: number;

  /**
   * @example: /6WxhEvFsauuACfv8HyoVX6mZKFj.jpg
   */
  poster_path: string;

  /**
   * @example: "2025-05-14"
   */
  release_date: string;

  /**
   * @example: "Final Destination Bloodlines"
   */
  title: string;

  /**
   * @example: false 
   */
  video: boolean;

  /**
   * @example: 7.2
   */
  vote_average: number;

  /**
   * @example: 830
   */
  vote_count: number;

}