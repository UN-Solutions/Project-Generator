require "test_helper"

class AwarenessesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @awareness = awarenesses(:one)
  end

  test "should get index" do
    get awarenesses_url
    assert_response :success
  end

  test "should get new" do
    get new_awareness_url
    assert_response :success
  end

  test "should create awareness" do
    assert_difference("Awareness.count") do
      post awarenesses_url, params: { awareness: { subject: @awareness.subject, subtopics: @awareness.subtopics, title: @awareness.title } }
    end

    assert_redirected_to awareness_url(Awareness.last)
  end

  test "should show awareness" do
    get awareness_url(@awareness)
    assert_response :success
  end

  test "should get edit" do
    get edit_awareness_url(@awareness)
    assert_response :success
  end

  test "should update awareness" do
    patch awareness_url(@awareness), params: { awareness: { subject: @awareness.subject, subtopics: @awareness.subtopics, title: @awareness.title } }
    assert_redirected_to awareness_url(@awareness)
  end

  test "should destroy awareness" do
    assert_difference("Awareness.count", -1) do
      delete awareness_url(@awareness)
    end

    assert_redirected_to awarenesses_url
  end
end
