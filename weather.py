{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "384537ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "import requests\n",
    "import time\n",
    "\n",
    "\n",
    "def getWeather(canvas):\n",
    "    city = textField.get()\n",
    "    api = \"https://api.openweathermap.org/data/2.5/weather?q=\" + city + \"&appid=06c921750b9a82d8f5d1294e1586276f\"\n",
    "\n",
    "    json_data = requests.get(api).json()\n",
    "    condition = json_data['weather'][0]['main']\n",
    "    temp = int(json_data['main']['temp'] - 273.15)\n",
    "    min_temp = int(json_data['main']['temp_min'] - 273.15)\n",
    "    max_temp = int(json_data['main']['temp_max'] - 273.15)\n",
    "    pressure = json_data['main']['pressure']\n",
    "    humidity = json_data['main']['humidity']\n",
    "    wind = json_data['wind']['speed']\n",
    "    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))\n",
    "    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))\n",
    "\n",
    "    final_info = condition + \"\\n\" + str(temp) + \"°C\"\n",
    "    final_data = \"\\n\" + \"Min Temp: \" + str(min_temp) + \"°C\" + \"\\n\" + \"Max Temp: \" + str(\n",
    "        max_temp) + \"°C\" + \"\\n\" + \"Pressure: \" + str(pressure) + \"\\n\" + \"Humidity: \" + str(\n",
    "        humidity) + \"\\n\" + \"Wind Speed: \" + str(wind) + \"\\n\" + \"Sunrise: \" + sunrise + \"\\n\" + \"Sunset: \" + sunset\n",
    "    label1.config(text=final_info)\n",
    "    label2.config(text=final_data)\n",
    "\n",
    "\n",
    "canvas = tk.Tk()\n",
    "canvas.geometry(\"600x500\")\n",
    "canvas.title(\"Weather App\")\n",
    "f = (\"poppins\", 15, \"bold\")\n",
    "t = (\"poppins\", 35, \"bold\")\n",
    "\n",
    "textField = tk.Entry(canvas, justify='center', width=20, font=t)\n",
    "textField.pack(pady=20)\n",
    "textField.focus()\n",
    "textField.bind('<Return>', getWeather)\n",
    "\n",
    "label1 = tk.Label(canvas, font=t)\n",
    "label1.pack()\n",
    "label2 = tk.Label(canvas, font=f)\n",
    "label2.pack()\n",
    "canvas.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef7b247f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
