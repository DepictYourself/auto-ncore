import "./App.css";
import Browser from "./components/browser";
import Downloads from "./components/Downloads";
import MovieDetail from "./components/movie-detail";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NotFoundPage from "./components/not-found-page";
import NavbarComponent from "./components/Navbar";

function App() {
  return (
    <>
      <BrowserRouter>
        <NavbarComponent />
        <Routes>
          <Route path="/" element={<Browser />} />
          <Route path="movie/:id" element={<MovieDetail />} />
          <Route path="downloads" element={<Downloads />} />
          <Route path="*" element={<NotFoundPage/>} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
