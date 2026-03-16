import { Database } from "bun:sqlite";
import * as sqliteVec from "sqlite-vec";

// macOS: Apple's system SQLite disables loadExtension().
if (process.platform === "darwin") {
  const brewSqlite = "/opt/homebrew/opt/sqlite/lib/libsqlite3.dylib";
  const { existsSync } = await import("node:fs");
  if (!existsSync(brewSqlite)) {
    console.error(`Homebrew SQLite not found at ${brewSqlite}`);
    console.error("Install it: brew install sqlite");
    process.exit(1);
  }
  Database.setCustomSQLite(brewSqlite);
}

const db = new Database(":memory:");
sqliteVec.load(db);

const version = db.query("SELECT vec_version()").get() as any;
console.log("sqlite-vec loaded successfully, version:", Object.values(version)[0]);
db.close();
