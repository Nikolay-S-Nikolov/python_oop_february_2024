from abc import ABC, abstractmethod
from typing import List

from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: List[BaseCampaign] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if not value.strip():
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value: int):
        """
        number of followers is a non-negative integer
        """
        if value < 0 or not isinstance(value, int):
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value: float):
        if not (0 <= value <= 5):
            raise ValueError("Engagement rate should be between 0 and 5.")
        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        ...

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        ...

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."
        result = [f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:"]

        for c in self.campaigns_participated:
            reached_followers = self.reached_followers(type(c).__name__)
            result.append(f"  - Campaign ID: {c.campaign_id}, Brand: {c.brand}, Reached followers: {reached_followers}")
        return '\n'.join(result)
