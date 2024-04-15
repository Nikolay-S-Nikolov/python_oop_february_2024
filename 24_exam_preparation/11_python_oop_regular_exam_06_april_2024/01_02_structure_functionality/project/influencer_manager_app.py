from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        valid_types = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}

        if influencer_type not in valid_types:
            return f"{influencer_type} is not an allowed influencer type."

        if [infl for infl in self.influencers if infl.username == username]:
            return f"{username} is already registered."

        new_influencer = valid_types[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        valid_types = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

        if campaign_type not in valid_types:
            return f"{campaign_type} is not a valid campaign type."

        if [c for c in self.campaigns if c.campaign_id == campaign_id]:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = valid_types[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):

        try:
            influencer = next(filter(lambda infl: infl.username == influencer_username, self.influencers))

        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))

        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        check_eligibility = campaign.check_eligibility(influencer.engagement_rate)

        if not check_eligibility:
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the " \
                   f"campaign with ID {campaign_id}."
        calculated_payment = influencer.calculate_payment(campaign)
        if calculated_payment > 0:
            campaign.approved_influencers.append(influencer)
            influencer.campaigns_participated.append(campaign)
            campaign.budget -= calculated_payment
            return f"Influencer '{influencer_username}' has successfully participated" \
                   f" in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):

        campaigns_with_influencers = [c for c in self.campaigns if c.approved_influencers]
        result = {}
        for campaign in campaigns_with_influencers:
            total_followers = sum(
                infl.reached_followers(type(campaign).__name__) for infl in campaign.approved_influencers
            )
            if total_followers > 0:
                result[campaign] = total_followers

        return result

    def influencer_campaign_report(self, username: str):
        influencer = [infl for infl in self.influencers if infl.username == username][0]

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):

        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = ["$$ Campaign Statistics $$"]
        c_info = [
            f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
            f"Total budget: ${c.budget:.2f}, Total reached followers: {self.calculate_total_reached_followers()[c]}"
            for c in sorted_campaigns
        ]
        result.extend(c_info)
        return '\n'.join(result)
