require "test_helper"

class MluserinputsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @mluserinput = mluserinputs(:one)
  end

  test "should get index" do
    get mluserinputs_url
    assert_response :success
  end

  test "should get new" do
    get new_mluserinput_url
    assert_response :success
  end

  test "should create mluserinput" do
    assert_difference("Mluserinput.count") do
      post mluserinputs_url, params: { mluserinput: { mlinput: @mluserinput.mlinput, subject: @mluserinput.subject, subtopics: @mluserinput.subtopics, title: @mluserinput.title } }
    end

    assert_redirected_to mluserinput_url(Mluserinput.last)
  end

  test "should show mluserinput" do
    get mluserinput_url(@mluserinput)
    assert_response :success
  end

  test "should get edit" do
    get edit_mluserinput_url(@mluserinput)
    assert_response :success
  end

  test "should update mluserinput" do
    patch mluserinput_url(@mluserinput), params: { mluserinput: { mlinput: @mluserinput.mlinput, subject: @mluserinput.subject, subtopics: @mluserinput.subtopics, title: @mluserinput.title } }
    assert_redirected_to mluserinput_url(@mluserinput)
  end

  test "should destroy mluserinput" do
    assert_difference("Mluserinput.count", -1) do
      delete mluserinput_url(@mluserinput)
    end

    assert_redirected_to mluserinputs_url
  end
end
