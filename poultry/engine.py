"""Poultry Hatchery Flock Management, Pearson Square Feed Formulation & FCR Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class HatcheryBatchAudit:
    flock_id: str
    total_eggs_set: int
    fertile_eggs_detected: int
    chicks_hatched_alive: int
    fertility_percentage: float
    hatchability_percentage: float
    cull_chicks_rejected: int


@dataclass
class FlockFCRPerformance:
    flock_id: str
    bird_age_days: int
    initial_birds_housed: int
    current_birds_alive: int
    total_feed_consumed_kg: float
    total_flock_weight_kg: float
    feed_conversion_ratio_fcr: float
    mortality_rate_pct: float
    performance_rating: str  # EXCELLENT (FCR < 1.55), AVERAGE, POOR


class PoultryHatcheryEngine:
    """Monitors setter/hatcher performance and broiler flock feed conversion metrics."""

    def audit_hatchery_batch(
        self,
        flock_id: str,
        eggs_set: int,
        fertile_eggs: int,
        chicks_hatched: int,
        cull_rejected: int
    ) -> HatcheryBatchAudit:
        fertility_pct = round((fertile_eggs / eggs_set) * 100.0, 2) if eggs_set > 0 else 0.0
        hatchability_pct = round((chicks_hatched / eggs_set) * 100.0, 2) if eggs_set > 0 else 0.0

        return HatcheryBatchAudit(
            flock_id=flock_id,
            total_eggs_set=eggs_set,
            fertile_eggs_detected=fertile_eggs,
            chicks_hatched_alive=chicks_hatched,
            fertility_percentage=fertility_pct,
            hatchability_percentage=hatchability_pct,
            cull_chicks_rejected=cull_rejected
        )

    def evaluate_flock_fcr(
        self,
        flock_id: str,
        age_days: int,
        initial_birds: int,
        current_birds: int,
        feed_consumed_kg: float,
        flock_weight_kg: float
    ) -> FlockFCRPerformance:
        # FCR = Total Feed Consumed (kg) / Total Live Body Weight (kg)
        fcr = round(feed_consumed_kg / flock_weight_kg, 2) if flock_weight_kg > 0 else 0.0
        mortality = round(((initial_birds - current_birds) / initial_birds) * 100.0, 2) if initial_birds > 0 else 0.0

        if fcr <= 1.55:
            rating = "EXCELLENT_EFFICIENCY"
        elif fcr <= 1.75:
            rating = "STANDARD_COMMERCIAL_EFFICIENCY"
        else:
            rating = "DEFICIENT_HIGH_FEED_LOSS"

        return FlockFCRPerformance(
            flock_id=flock_id,
            bird_age_days=age_days,
            initial_birds_housed=initial_birds,
            current_birds_alive=current_birds,
            total_feed_consumed_kg=feed_consumed_kg,
            total_flock_weight_kg=flock_weight_kg,
            feed_conversion_ratio_fcr=fcr,
            mortality_rate_pct=mortality,
            performance_rating=rating
        )
