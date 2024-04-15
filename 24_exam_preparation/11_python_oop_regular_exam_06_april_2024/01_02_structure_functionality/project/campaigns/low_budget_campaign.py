from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2_500

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        """
        This method takes an engagement_rate parameter. The influencer is eligible for the campaign only if
        their engagement rate is greater than or equal to 90% of the required engagement rate.
        """
        return engagement_rate >= self.required_engagement * 0.9
