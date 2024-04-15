from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        calculated_payment = campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE
        return calculated_payment

    def reached_followers(self, campaign_type: str):
        campaign_types = {"HighBudgetCampaign": 1.2, "LowBudgetCampaign": 0.9}
        reached_followers = int((self.followers * self.engagement_rate) * campaign_types[campaign_type])
        return reached_followers

