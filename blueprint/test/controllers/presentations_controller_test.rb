require "test_helper"

class PresentationsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @presentation = presentations(:one)
  end

  test "should get index" do
    get presentations_url
    assert_response :success
  end

  test "should get new" do
    get new_presentation_url
    assert_response :success
  end

  test "should create presentation" do
    assert_difference("Presentation.count") do
      post presentations_url, params: { presentation: { subject: @presentation.subject, subtopics: @presentation.subtopics, title: @presentation.title } }
    end

    assert_redirected_to presentation_url(Presentation.last)
  end

  test "should show presentation" do
    get presentation_url(@presentation)
    assert_response :success
  end

  test "should get edit" do
    get edit_presentation_url(@presentation)
    assert_response :success
  end

  test "should update presentation" do
    patch presentation_url(@presentation), params: { presentation: { subject: @presentation.subject, subtopics: @presentation.subtopics, title: @presentation.title } }
    assert_redirected_to presentation_url(@presentation)
  end

  test "should destroy presentation" do
    assert_difference("Presentation.count", -1) do
      delete presentation_url(@presentation)
    end

    assert_redirected_to presentations_url
  end
end
