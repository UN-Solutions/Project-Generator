require "test_helper"

class UserinputsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @userinput = userinputs(:one)
  end

  test "should get index" do
    get userinputs_url
    assert_response :success
  end

  test "should get new" do
    get new_userinput_url
    assert_response :success
  end

  test "should create userinput" do
    assert_difference("Userinput.count") do
      post userinputs_url, params: { userinput: { subject: @userinput.subject, subtopics: @userinput.subtopics, title: @userinput.title } }
    end

    assert_redirected_to userinput_url(Userinput.last)
  end

  test "should show userinput" do
    get userinput_url(@userinput)
    assert_response :success
  end

  test "should get edit" do
    get edit_userinput_url(@userinput)
    assert_response :success
  end

  test "should update userinput" do
    patch userinput_url(@userinput), params: { userinput: { subject: @userinput.subject, subtopics: @userinput.subtopics, title: @userinput.title } }
    assert_redirected_to userinput_url(@userinput)
  end

  test "should destroy userinput" do
    assert_difference("Userinput.count", -1) do
      delete userinput_url(@userinput)
    end

    assert_redirected_to userinputs_url
  end
end
