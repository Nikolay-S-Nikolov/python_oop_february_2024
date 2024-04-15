from abc import ABC, abstractmethod


class BaseCampaign(ABC):
    created_id = []

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand  # string representing the name of the brand
        self.budget = budget
        self.required_engagement = required_engagement  # floating-point number representing the minimum engagement
        # rate required for an influencer to be eligible for the campaign
        self.approved_influencers: list = []  # maybe objects

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value: int):
        self.validate_id(value)
        if value <= 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")

        self.__campaign_id = value

    def validate_id(self, value):
        if value in self.created_id:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self.created_id.append(value)

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        """
        This method is designed to determine whether an influencer is eligible to participate in a
        campaign based on their engagement rate.
        """
        ...
