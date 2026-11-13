-- QA A: accounts gain a tier column
ALTER TABLE accounts ADD COLUMN tier TEXT NOT NULL DEFAULT 'basic';
