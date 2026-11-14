import unittest
from poultry.engine import PoultryHatcheryEngine

class TestPoultryHatchery(unittest.TestCase):
    def test_hatchery_audit_and_fcr(self):
        engine = PoultryHatcheryEngine()

        audit = engine.audit_hatchery_batch(
            flock_id="HATCH-2026-B1",
            eggs_set=10000,
            fertile_eggs=9200,
            chicks_hatched=8500,
            cull_rejected=100
        )
        self.assertEqual(audit.fertility_percentage, 92.0)
        self.assertEqual(audit.hatchability_percentage, 85.0)

        fcr = engine.evaluate_flock_fcr(
            flock_id="BROILER-SHED-04",
            age_days=35,
            initial_birds=5000,
            current_birds=4850,
            feed_consumed_kg=15000.0,
            flock_weight_kg=10000.0
        )
        # FCR = 15000 / 10000 = 1.50
        self.assertEqual(fcr.feed_conversion_ratio_fcr, 1.50)
        self.assertEqual(fcr.performance_rating, "EXCELLENT_EFFICIENCY")
        self.assertEqual(fcr.mortality_rate_pct, 3.0)

if __name__ == "__main__":
    unittest.main()
