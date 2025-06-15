/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_BACKEND_URL: string
    readonly VITE_TMDB_IMG_URL: string
}

interface ImportMeta {
    readonly env: ImportMetaEnv
}