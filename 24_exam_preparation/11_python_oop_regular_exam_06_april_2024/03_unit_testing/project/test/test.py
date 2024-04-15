from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.media = SocialMedia("Test", 'YouTube', 20, "test content")

    def test_correct_init(self):
        self.assertEqual("Test", self.media._username)
        self.assertEqual("YouTube", self.media._platform)
        self.assertEqual(20, self.media._followers)
        self.assertEqual("test content", self.media._content_type)
        self.assertEqual([], self.media._posts)

    def test_setter_platform_return_correct_message_when_incorrect_data(self):
        with self.assertRaises(ValueError) as ve:
            self.media.platform = "test platform"
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_setter_followers_return_correct_message_when_incorrect_data(self):
        with self.assertRaises(ValueError) as ve:
            self.media.followers = -1
        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_validate_and_set_platform_with_incorrect_data(self):
        with self.assertRaises(ValueError) as ve:
            self.media._validate_and_set_platform("test platform")
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_validate_and_set_platform_with_correct_data(self):
        self.assertEqual('YouTube', self.media.platform)
        self.media._validate_and_set_platform("Twitter")
        self.assertEqual('Twitter', self.media.platform)

    def test_create_post_return_correct_message(self):
        result = 'New test content post created by Test on YouTube.'
        self.assertEqual(result, self.media.create_post("test post"))
        self.assertEqual([{'comments': [], 'content': 'test post', 'likes': 0}], self.media._posts)

    def test_like_post_return_messages(self):
        self.media.create_post("test post")
        self.assertEqual('Post liked by Test.', self.media.like_post(0))
        self.assertEqual([{'comments': [], 'content': 'test post', 'likes': 1}], self.media._posts)
        self.assertEqual('Invalid post index.', self.media.like_post(3))
        self.assertEqual([{'comments': [], 'content': 'test post', 'likes': 1}], self.media._posts)

        for _ in range(9):
            self.media.like_post(0)
        self.assertEqual('Post has reached the maximum number of likes.', self.media.like_post(0))
        self.assertEqual([{'comments': [], 'content': 'test post', 'likes': 10}], self.media._posts)

    def test_comment_on_post_return_correct_messages(self):
        self.media.create_post("test post")
        self.assertEqual('Comment added by Test on the post.', self.media.comment_on_post(0, "Test comment"))
        expected = [{'comments': [{'comment': 'Test comment', 'user': 'Test'}], 'content': 'test post', 'likes': 0}]
        self.assertEqual(expected, self.media._posts)
        self.assertEqual('Comment should be more than 10 characters.', self.media.comment_on_post(0, "Test comme"))
        self.assertEqual(expected, self.media._posts)
        self.assertEqual('Comment should be more than 10 characters.', self.media.comment_on_post(0, ""))
        self.assertEqual(expected, self.media._posts)


if __name__ == "__main__":
    main()
