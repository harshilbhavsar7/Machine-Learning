_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py', '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py'
]
model = dict(roi_head=dict(bbox_head=dict(num_classes=27)))
# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# actual epoch = 3 * 3 = 9
lr_config = dict(policy='step', step=[3])
# runtime settings
# total_epochs = 4  # actual epoch = 4 * 3 = 12

dataset_type = 'VOCDataset'
data_root = '/content/data/VOCdevkit/VOC2007'
data = dict(
    train=dict(
        dataset=dict(
            type='VOCDataset',
            ann_file=data_root+'/Main/train.txt',
            img_prefix='/content/data/VOCdevkit/VOC2007/',
            )),
    val=dict(
        type='VOCDataset',
        ann_file=data_root+'/Main/val.txt',
        img_prefix='/content/data/VOCdevkit/VOC2007/',
        ),
    test=dict(
        type='VOCDataset',
        ann_file=data_root+'/Main/test.txt',
        img_prefix='/content/data/VOCdevkit/VOC2007/',
        ))
total_epochs = 50
checkpoint_config = dict(interval=5)

log_config = dict(  # config to register logger hook
    interval=50,  # Interval to print the log
    hooks=[
        dict(type='TensorboardLoggerHook')  # The Tensorboard logger is also supported
        # dict(type='TextLoggerHook')
    ]) 


# %load_ext tensorboard
# !tensorboard --logdir /content/work_dir/faster_rcnn_r101_fpn_1x/tf_log