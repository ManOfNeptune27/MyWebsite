export interface Game {
  title: string;
  hours: number;
  platform: string;
  completion?: number;
  completionDate?: string;
  achievements_unlocked?: number;
  achievements_total?: number;
  achievements_completion?: number;
}

const fallbackGames: Game[] = [
  { title: 'Hollow Knight', completionDate: '2023-06-15', hours: 45, platform: 'Steam', completion: 100 },
  { title: 'Celeste', completionDate: '2023-04-22', hours: 28, platform: 'PlayStation', completion: 100 },
  { title: 'Hades', completionDate: '2023-08-10', hours: 52, platform: 'PlayStation', completion: 100 },
  { title: 'Stardew Valley', completionDate: '2024-02-14', hours: 180, platform: 'Steam', completion: 100 },
  { title: 'God of War', completionDate: '2024-01-20', hours: 35, platform: 'PlayStation', completion: 85 },
  { title: "Baldur's Gate 3", completionDate: '2024-03-10', hours: 120, platform: 'Steam', completion: 78 }
];

const snapshotModules = import.meta.glob<Game[]>('./games.json', {
  eager: true,
  import: 'default'
});

export const games: Game[] = Object.values(snapshotModules)[0] ?? fallbackGames;
