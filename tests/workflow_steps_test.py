from hn_sentiment.app import (
    AnalyseSentiment,
    CreateMarkdown,
    GetHackerNewsComments,
    GetHackerNewsStory,
    WriteMarkdownToFile,
    workflow,
)


def test_return_expected_workflow() -> None:
    expected_workflow_steps = workflow()

    assert expected_workflow_steps == [
        GetHackerNewsStory,
        GetHackerNewsComments,
        AnalyseSentiment,
        CreateMarkdown,
        WriteMarkdownToFile,
    ]
