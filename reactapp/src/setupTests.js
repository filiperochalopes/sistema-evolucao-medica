import { fetch, Request, Response } from "cross-fetch";
if (!globalThis.fetch) {
  globalThis.fetch = fetch;
  globalThis.Request = Request;
  globalThis.Response = Response;
}
