// scripts/lib/db.ts
import { Database } from "bun:sqlite";
import * as sqliteVec from "sqlite-vec";
import { existsSync } from "node:fs";

// macOS: Apple's system SQLite disables loadExtension().
if (process.platform === "darwin") {
  const brewSqlite = "/opt/homebrew/opt/sqlite/lib/libsqlite3.dylib";
  if (!existsSync(brewSqlite)) {
    console.error(`Homebrew SQLite not found at ${brewSqlite}`);
    console.error("Install it: brew install sqlite");
    process.exit(1);
  }
  Database.setCustomSQLite(brewSqlite);
}

export function openDb(path: string): Database {
  const db = new Database(path);
  sqliteVec.load(db);

  db.run(`
    CREATE TABLE IF NOT EXISTS meta (
      key TEXT PRIMARY KEY,
      value TEXT NOT NULL
    )
  `);

  db.run(`
    CREATE TABLE IF NOT EXISTS embedding_records (
      id TEXT PRIMARY KEY,
      slug TEXT NOT NULL,
      kind TEXT NOT NULL,
      section TEXT NOT NULL,
      text TEXT NOT NULL,
      model TEXT,
      model_version TEXT,
      created_at TEXT NOT NULL
    )
  `);

  db.run(`CREATE INDEX IF NOT EXISTS idx_records_slug ON embedding_records(slug)`);
  db.run(`CREATE INDEX IF NOT EXISTS idx_records_section ON embedding_records(section)`);

  return db;
}

// Self-test
if (import.meta.main) {
  const db = openDb(":memory:");
  const vecVersion = db.query("SELECT vec_version()").get() as any;
  console.log("DB module OK, sqlite-vec:", Object.values(vecVersion)[0]);
  db.close();
}
