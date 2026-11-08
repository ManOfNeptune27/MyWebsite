export interface Favorite {
  id: number;
  name: string;
  rating: number;
  details: string;
}

export const movieFavorites: Favorite[] = [
  { id: 4, name: 'Inception', rating: 9.5, details: 'Mind-bending sci-fi masterpiece with stunning visuals and an intricate plot about shared dreams and consciousness.' },
  { id: 5, name: 'The Matrix', rating: 9, details: 'Groundbreaking cyberpunk film with philosophical depth and revolutionary action sequences for its time.' }
];
