_base_ = '../cascade_rcnn/cascade_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://msra/hrnetv2_w32',
    backbone=dict(
        _delete_=True,
        type='HRNet',
        extra=dict(
            stage1=dict(
                num_modules=1,
                num_branches=1,
                block='BOTTLENECK',

                num_blocks=(4, ),
                num_channels=(64, )),
            stage2=dict(
                num_modules=1,
                num_branches=2,
                block='BASIC',
                num_blocks=(4, 4),
                num_channels=(32, 64)),
            stage3=dict(
                num_modules=4,
                num_branches=3,
                block='BASIC',
                num_blocks=(4, 4, 4),
                num_channels=(32, 64, 128)),
            stage4=dict(
                num_modules=3,
                num_branches=4,
                block='BASIC',
                num_blocks=(4, 4, 4, 4),
                num_channels=(32, 64, 128, 256)))),
    neck=dict(
        _delete_=True,
        type='HRFPN',
        in_channels=[32, 64, 128, 256],
        out_channels=256))

dataset_type = 'CocoDataset'
# data_root = 'data/coco/'
classes=('table', 'cell')
data = dict(
    type='ClassBalancedDataset',
    oversample_thr=1e-5,
    train=dict(
        type='CocoDataset',
        classes=classes,
        ann_file='/content/data/coco/annotations/train.json',
        img_prefix='/content/data/coco/JPEGImages',
       ),
    val=dict(
        type='CocoDataset',
        classes=classes,
        ann_file='/content/data/coco/annotations/val.json',
        img_prefix='/content/data/coco/JPEGImages',
        ),
    test=dict(
        type='CocoDataset',
        classes=classes,
        ann_file='/content/data/coco/annotations/test.json',
        img_prefix='/content/data/coco/JPEGImages',
       ))

optimizer = dict(type='SGD', lr=0.001, momentum=0.9)

total_epochs = 50
checkpoint_config = dict(interval=1)
log_config = dict(interval=5, hooks=[dict(type='TextLoggerHook')])
load_from = None
resume_from = None
workflow = [('train', 1)]
