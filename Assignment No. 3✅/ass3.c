#include <stdio.h>
#include <omp.h>
#include <unistd.h>

#define N 100
#define NUM_PROCESSORS 4

int main()
{
    int arr[N];
    for (int i = 0; i < N; i++)
    {
        arr[i] = 4 * i;
    }

    int sum = 0;
    int PARTIAL_SUM[NUM_PROCESSORS] = {0};
    omp_set_num_threads(NUM_PROCESSORS);

#pragma omp parallel
    {
        // int thread_id = omp_get_thread_num();
        // int start = thread_id * (N / NUM_PROCESSORS);
        // int end = (thread_id + 1) * (N / NUM_PROCESSORS);

        // for (int i = start; i < end; i++)
        // {
        //     PARTIAL_SUM[thread_id] += arr[i];
        // }
        for (int i = 0; i < 5; i++)
        {
            sleep(omp_get_thread_num());
            printf("Thread %d is sleeping for 3 seconds\n", omp_get_thread_num());
        }
    }

    for (int i = 0; i < NUM_PROCESSORS; i++)
    {
        sum += PARTIAL_SUM[i];
        printf("Partial sum of thread %d: %d\n", i, PARTIAL_SUM[i]);
    }

    printf("Total sum: %d\n", sum);

    return 0;
}
