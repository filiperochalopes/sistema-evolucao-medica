import { fetch, Request, Response } from "cross-fetch";

/* global globalThis */

if (!globalThis.fetch) {
  globalThis.fetch = fetch;
  globalThis.Request = Request;
  globalThis.Response = Response;
}
