class ProfessionalsController < ApplicationController
  before_action :set_professional, only: %i[ show edit update destroy ]
  def download_pdf
    send_file "#{Rails.root}/prof.pdf", type: "application/pdf", x_sendfile: true
  end
  # GET /professionals or /professionals.json
  def index
    @professionals = Professional.all
    @our_input = Professional.order("id DESC").first

    # Convert the data to a JSON string and write it to a file
    File.write("input.txt", @our_input.to_json)

    # Call the Python script with the input file as an argument
    @output = `/home/hung/miniconda3/envs/bp/bin/python3 prof.py input.txt`
  end

  # GET /professionals/1 or /professionals/1.json
  def show
  end

  # GET /professionals/new
  def new
    @professional = Professional.new
  end

  # GET /professionals/1/edit
  def edit
  end

  # POST /professionals or /professionals.json
  def create
    @professional = Professional.new(professional_params)

    respond_to do |format|
      if @professional.save
        format.html { redirect_to professional_url(@professional), notice: "Professional was successfully created." }
        format.json { render :show, status: :created, location: @professional }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @professional.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /professionals/1 or /professionals/1.json
  def update
    respond_to do |format|
      if @professional.update(professional_params)
        format.html { redirect_to professional_url(@professional), notice: "Professional was successfully updated." }
        format.json { render :show, status: :ok, location: @professional }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @professional.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /professionals/1 or /professionals/1.json
  def destroy
    @professional.destroy

    respond_to do |format|
      format.html { redirect_to professionals_url, notice: "Professional was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_professional
      @professional = Professional.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def professional_params
      params.require(:professional).permit(:company, :slogan, :about, :looking, :benefits, :address, :phone, :email)
    end
end
