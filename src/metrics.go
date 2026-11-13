package metrics

var rejected = promauto.NewCounterVec(prometheus.CounterOpts{Name: "trades_rejected_total"}, []string{"reason"})
