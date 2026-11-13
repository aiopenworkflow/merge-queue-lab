module.exports = (app) => {
  app.post("/v1/refunds", async (req, res) => { res.status(202).json({ queued: true }); });
  app.get("/v1/refunds/:id", async (req, res) => { res.json({ id: req.params.id, state: "queued" }); });
};
