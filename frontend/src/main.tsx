import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './index.css'
import App from './App.tsx'
import NotFoundPage from './components/not-found-page.tsx';
import MovieDetail from './components/movie-detail.tsx';

const router = createBrowserRouter([
  { path: "/", element: <App /> },
  { path: "/movie/:id", element: <MovieDetail />},
  { path: "*", element: <NotFoundPage />}
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
