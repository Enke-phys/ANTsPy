#Training starten
python train.py \
  --dataroot ./datasets/facades \
  --name facades_pix2pix \
  --model pix2pix \
  --direction BtoA
echo "Training gestartet."

#Testen des trainierten Modells
#python test.py \
#  --dataroot ./datasets/facades \
#  --name facades_pix2pix \
#  --model pix2pix \
#  --direction BtoA
#echo "Test abgeschlossen. Ergebnisse in ./results/facades_pix2pix/test_latest/"

