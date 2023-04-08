require "application_system_test_case"

class ProfessionalsTest < ApplicationSystemTestCase
  setup do
    @professional = professionals(:one)
  end

  test "visiting the index" do
    visit professionals_url
    assert_selector "h1", text: "Professionals"
  end

  test "should create professional" do
    visit professionals_url
    click_on "New professional"

    fill_in "About", with: @professional.about
    fill_in "Address", with: @professional.address
    fill_in "Benefits", with: @professional.benefits
    fill_in "Company", with: @professional.company
    fill_in "Email", with: @professional.email
    fill_in "Looking", with: @professional.looking
    fill_in "Phone", with: @professional.phone
    fill_in "Slogan", with: @professional.slogan
    click_on "Create Professional"

    assert_text "Professional was successfully created"
    click_on "Back"
  end

  test "should update Professional" do
    visit professional_url(@professional)
    click_on "Edit this professional", match: :first

    fill_in "About", with: @professional.about
    fill_in "Address", with: @professional.address
    fill_in "Benefits", with: @professional.benefits
    fill_in "Company", with: @professional.company
    fill_in "Email", with: @professional.email
    fill_in "Looking", with: @professional.looking
    fill_in "Phone", with: @professional.phone
    fill_in "Slogan", with: @professional.slogan
    click_on "Update Professional"

    assert_text "Professional was successfully updated"
    click_on "Back"
  end

  test "should destroy Professional" do
    visit professional_url(@professional)
    click_on "Destroy this professional", match: :first

    assert_text "Professional was successfully destroyed"
  end
end
