from nephthys.transcripts.transcript import Transcript


class ThirdSpace(Transcript):
    """Transcript for Third Space"""

    program_name: str = "third space"
    program_owner: str = "U..."  # replace with your Slack user ID

    help_channel: str = "C0BQ2MRAZ6F"  # third-space-help
    ticket_channel: str = ""  # third-space-tickets (set via SLACK_TICKET_CHANNEL env var)
    team_channel: str = ""  # third-space-bts (set via SLACK_BTS_CHANNEL env var)

    faq_link: str = "https://hackclub.slack.com/docs/T0266FRGM/F093F8D7EE9"

    first_ticket_create: str = f"""
hi (user)! welcome to third space! someone will be here soon to help answer your question. in the meantime, feel free to check out the <{faq_link}|faq> for common questions.
if your question has been answered, please hit the button below to mark it as resolved ^-^
"""
    ticket_create: str = f"someone will be here soon to help answer your question! in the meantime, feel free to check out the <{faq_link}|faq> for common questions. if your question has been answered, please hit the button below to mark it as resolved ^-^"
    resolve_ticket_button: str = "i get it now"
    ticket_resolve: str = f"oh, oh! it looks like this post has been marked as resolved by <@{{user_id}}>! if you have any more questions, please make a new post in <#{help_channel}> and someone'll be happy to help you out! not me though, i'm just a silly raccoon ^-^"

    not_allowed_channel: str = f"heyo! doesn't seem like you're supposed to be in that channel, please reach out to <@{program_owner}> if that's wrong!"
