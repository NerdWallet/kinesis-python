import os

from kinesis.producer import KinesisProducer


def test_producer(mocker):
    mocked_async_producer = mocker.patch('kinesis.producer.AsyncProducer')
    producer = KinesisProducer('testing')
    mocked_async_producer.assert_called_with(
        'testing',
        0.5,
        producer.queue,
        max_count=None,
        max_size=None,
        boto3_session=None
    )

    mocked_queue = mocker.patch.object(producer, 'queue')
    producer.put('foo', explicit_hash_key='hash', partition_key='partition')
    mocked_queue.put.assert_called_with(('foo', 'hash', 'partition'))
