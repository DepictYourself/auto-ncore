import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './index.css'
import App from './App.tsx'
import NotFoundPage from './components/not-found-page.tsx';
import MovieDetail from './components/movie-detail.tsx';
import Downloads from './components/Downloads.tsx';

const router = createBrowserRouter([
  { path: "/", element: <App /> },
  { path: "/movie/:id", element: <MovieDetail />},
  { path: "/downloads", element: <Downloads />},
  { path: "*", element: <NotFoundPage />}
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
