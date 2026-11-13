const client = require("prom-client");
const timeoutMs = Number(process.env.QA_C_TIMEOUT_MS || 500);
const upstreamToken = process.env.QA_C_UPSTREAM_TOKEN;
const exportFailures = new client.Counter({ name: "qa_export_failures_total", help: "exports that failed", labelNames: ["reason"] });
module.exports = (app) => {
  app.get("/v1/exports/:id", async (req, res) => { res.json({ id: req.params.id, timeoutMs, auth: !!upstreamToken }); });
};
