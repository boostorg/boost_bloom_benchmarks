# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.70</td>
    <td align="right">7.84</td>
    <td align="right">4.40</td>
    <td align="right">13.64</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.10</td>
    <td align="right">11.91</td>
    <td align="right">18.46</td>
    <td align="right">17.01</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.02</td>
    <td align="right">4.38</td>
    <td align="right">4.71</td>
    <td align="right">11.22</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.47</td>
    <td align="right">4.80</td>
    <td align="right">5.16</td>
    <td align="right">11.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.44</td>
    <td align="right">17.74</td>
    <td align="right">19.24</td>
    <td align="right">21.08</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">4.85</td>
    <td align="right">4.83</td>
    <td align="right">11.62</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.00</td>
    <td align="right">5.41</td>
    <td align="right">5.20</td>
    <td align="right">11.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.43</td>
    <td align="right">21.50</td>
    <td align="right">18.09</td>
    <td align="right">23.23</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.01</td>
    <td align="right">5.37</td>
    <td align="right">5.06</td>
    <td align="right">12.03</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.54</td>
    <td align="right">5.73</td>
    <td align="right">5.65</td>
    <td align="right">12.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.17</td>
    <td align="right">27.42</td>
    <td align="right">18.38</td>
    <td align="right">27.42</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.40</td>
    <td align="right">5.73</td>
    <td align="right">5.62</td>
    <td align="right">12.37</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">6.05</td>
    <td align="right">5.96</td>
    <td align="right">12.82</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.08</td>
    <td align="right">13.10</td>
    <td align="right">13.53</td>
    <td align="right">19.37</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.01</td>
    <td align="right">4.34</td>
    <td align="right">4.68</td>
    <td align="right">11.22</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.47</td>
    <td align="right">4.80</td>
    <td align="right">5.16</td>
    <td align="right">11.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.78</td>
    <td align="right">21.01</td>
    <td align="right">18.29</td>
    <td align="right">27.41</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">5.09</td>
    <td align="right">4.85</td>
    <td align="right">4.83</td>
    <td align="right">11.59</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">5.42</td>
    <td align="right">5.21</td>
    <td align="right">11.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.40</td>
    <td align="right">24.63</td>
    <td align="right">21.25</td>
    <td align="right">31.16</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.01</td>
    <td align="right">5.37</td>
    <td align="right">5.06</td>
    <td align="right">12.06</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">5.75</td>
    <td align="right">5.67</td>
    <td align="right">12.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.32</td>
    <td align="right">29.63</td>
    <td align="right">25.91</td>
    <td align="right">36.45</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.40</td>
    <td align="right">5.73</td>
    <td align="right">5.63</td>
    <td align="right">12.37</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.83</td>
    <td align="right">6.04</td>
    <td align="right">5.94</td>
    <td align="right">12.82</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">9.96</td>
    <td align="right">11.48</td>
    <td align="right">19.48</td>
    <td align="right">16.68</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.98</td>
    <td align="right">4.16</td>
    <td align="right">4.51</td>
    <td align="right">10.77</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.42</td>
    <td align="right">4.64</td>
    <td align="right">4.82</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.88</td>
    <td align="right">17.44</td>
    <td align="right">20.59</td>
    <td align="right">20.12</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.34</td>
    <td align="right">4.74</td>
    <td align="right">4.63</td>
    <td align="right">11.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">5.18</td>
    <td align="right">5.07</td>
    <td align="right">11.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.53</td>
    <td align="right">20.85</td>
    <td align="right">20.18</td>
    <td align="right">22.76</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.22</td>
    <td align="right">5.05</td>
    <td align="right">12.07</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.52</td>
    <td align="right">5.70</td>
    <td align="right">5.43</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.56</td>
    <td align="right">27.25</td>
    <td align="right">20.27</td>
    <td align="right">27.20</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.75</td>
    <td align="right">5.46</td>
    <td align="right">12.42</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.97</td>
    <td align="right">6.10</td>
    <td align="right">5.91</td>
    <td align="right">12.85</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">9.96</td>
    <td align="right">13.20</td>
    <td align="right">12.99</td>
    <td align="right">19.65</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.99</td>
    <td align="right">4.17</td>
    <td align="right">4.53</td>
    <td align="right">10.82</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.42</td>
    <td align="right">4.64</td>
    <td align="right">4.83</td>
    <td align="right">11.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.96</td>
    <td align="right">20.90</td>
    <td align="right">16.16</td>
    <td align="right">25.91</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.35</td>
    <td align="right">4.76</td>
    <td align="right">4.63</td>
    <td align="right">11.36</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">5.19</td>
    <td align="right">5.08</td>
    <td align="right">11.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.51</td>
    <td align="right">25.90</td>
    <td align="right">19.92</td>
    <td align="right">32.32</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.23</td>
    <td align="right">5.05</td>
    <td align="right">12.14</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.52</td>
    <td align="right">5.71</td>
    <td align="right">5.44</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.69</td>
    <td align="right">32.08</td>
    <td align="right">25.33</td>
    <td align="right">38.88</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.74</td>
    <td align="right">5.46</td>
    <td align="right">12.42</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.95</td>
    <td align="right">6.09</td>
    <td align="right">5.90</td>
    <td align="right">12.84</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.08</td>
    <td align="right">5.76</td>
    <td align="right">14.45</td>
    <td align="right">12.14</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.50</td>
    <td align="right">7.36</td>
    <td align="right">15.00</td>
    <td align="right">12.96</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.29</td>
    <td align="right">3.14</td>
    <td align="right">3.63</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">8.49</td>
    <td align="right">15.04</td>
    <td align="right">14.34</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.03</td>
    <td align="right">9.41</td>
    <td align="right">16.50</td>
    <td align="right">15.98</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">2.95</td>
    <td align="right">2.86</td>
    <td align="right">11.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.16</td>
    <td align="right">12.20</td>
    <td align="right">16.27</td>
    <td align="right">17.17</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.11</td>
    <td align="right">12.12</td>
    <td align="right">17.39</td>
    <td align="right">17.68</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.79</td>
    <td align="right">6.32</td>
    <td align="right">4.16</td>
    <td align="right">15.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.40</td>
    <td align="right">13.51</td>
    <td align="right">15.46</td>
    <td align="right">18.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.65</td>
    <td align="right">14.49</td>
    <td align="right">17.83</td>
    <td align="right">19.86</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.84</td>
    <td align="right">6.35</td>
    <td align="right">4.15</td>
    <td align="right">15.04</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">5.99</td>
    <td align="right">6.17</td>
    <td align="right">12.55</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.51</td>
    <td align="right">7.23</td>
    <td align="right">7.27</td>
    <td align="right">13.66</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.26</td>
    <td align="right">3.15</td>
    <td align="right">3.64</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.88</td>
    <td align="right">8.05</td>
    <td align="right">8.02</td>
    <td align="right">14.25</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.04</td>
    <td align="right">9.54</td>
    <td align="right">9.37</td>
    <td align="right">16.76</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.94</td>
    <td align="right">2.87</td>
    <td align="right">11.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.13</td>
    <td align="right">12.05</td>
    <td align="right">11.34</td>
    <td align="right">17.06</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.11</td>
    <td align="right">13.32</td>
    <td align="right">13.39</td>
    <td align="right">20.12</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.77</td>
    <td align="right">5.82</td>
    <td align="right">5.61</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.37</td>
    <td align="right">12.90</td>
    <td align="right">12.91</td>
    <td align="right">18.95</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.63</td>
    <td align="right">14.86</td>
    <td align="right">14.75</td>
    <td align="right">21.69</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.86</td>
    <td align="right">5.88</td>
    <td align="right">5.61</td>
    <td align="right">14.35</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">4.69</td>
    <td align="right">5.70</td>
    <td align="right">14.49</td>
    <td align="right">12.80</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.46</td>
    <td align="right">7.15</td>
    <td align="right">14.81</td>
    <td align="right">12.79</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.93</td>
    <td align="right">3.28</td>
    <td align="right">3.67</td>
    <td align="right">11.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.10</td>
    <td align="right">8.48</td>
    <td align="right">15.08</td>
    <td align="right">14.07</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.84</td>
    <td align="right">9.31</td>
    <td align="right">16.29</td>
    <td align="right">15.23</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.55</td>
    <td align="right">3.14</td>
    <td align="right">3.06</td>
    <td align="right">12.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.56</td>
    <td align="right">11.94</td>
    <td align="right">16.17</td>
    <td align="right">16.97</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.16</td>
    <td align="right">11.93</td>
    <td align="right">16.71</td>
    <td align="right">16.83</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.26</td>
    <td align="right">6.01</td>
    <td align="right">3.86</td>
    <td align="right">14.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.09</td>
    <td align="right">13.62</td>
    <td align="right">15.28</td>
    <td align="right">18.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.51</td>
    <td align="right">14.29</td>
    <td align="right">17.53</td>
    <td align="right">18.52</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.32</td>
    <td align="right">6.07</td>
    <td align="right">3.86</td>
    <td align="right">14.90</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">4.68</td>
    <td align="right">5.86</td>
    <td align="right">5.95</td>
    <td align="right">12.10</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.45</td>
    <td align="right">7.08</td>
    <td align="right">7.16</td>
    <td align="right">13.64</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.98</td>
    <td align="right">3.26</td>
    <td align="right">3.70</td>
    <td align="right">12.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.10</td>
    <td align="right">8.14</td>
    <td align="right">8.08</td>
    <td align="right">14.18</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.83</td>
    <td align="right">9.35</td>
    <td align="right">9.24</td>
    <td align="right">16.72</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.56</td>
    <td align="right">3.18</td>
    <td align="right">3.07</td>
    <td align="right">12.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.53</td>
    <td align="right">11.15</td>
    <td align="right">10.95</td>
    <td align="right">16.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.19</td>
    <td align="right">11.98</td>
    <td align="right">11.76</td>
    <td align="right">18.86</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.26</td>
    <td align="right">5.52</td>
    <td align="right">5.38</td>
    <td align="right">14.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.06</td>
    <td align="right">12.28</td>
    <td align="right">12.22</td>
    <td align="right">18.31</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.50</td>
    <td align="right">14.61</td>
    <td align="right">14.40</td>
    <td align="right">21.43</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.31</td>
    <td align="right">5.55</td>
    <td align="right">5.39</td>
    <td align="right">14.23</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.21</td>
    <td align="right">2.97</td>
    <td align="right">3.40</td>
    <td align="right">11.71</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.63</td>
    <td align="right">4.72</td>
    <td align="right">5.04</td>
    <td align="right">14.65</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.80</td>
    <td align="right">4.48</td>
    <td align="right">4.78</td>
    <td align="right">14.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.34</td>
    <td align="right">3.09</td>
    <td align="right">2.97</td>
    <td align="right">11.78</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.47</td>
    <td align="right">4.27</td>
    <td align="right">4.12</td>
    <td align="right">14.28</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.83</td>
    <td align="right">4.60</td>
    <td align="right">4.59</td>
    <td align="right">14.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.88</td>
    <td align="right">3.95</td>
    <td align="right">15.22</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.70</td>
    <td align="right">8.32</td>
    <td align="right">6.13</td>
    <td align="right">17.91</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.81</td>
    <td align="right">8.20</td>
    <td align="right">6.10</td>
    <td align="right">17.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.61</td>
    <td align="right">5.90</td>
    <td align="right">3.94</td>
    <td align="right">14.90</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.57</td>
    <td align="right">9.49</td>
    <td align="right">6.15</td>
    <td align="right">19.44</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.61</td>
    <td align="right">9.02</td>
    <td align="right">6.29</td>
    <td align="right">18.47</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.19</td>
    <td align="right">2.97</td>
    <td align="right">3.40</td>
    <td align="right">11.71</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.66</td>
    <td align="right">4.71</td>
    <td align="right">5.04</td>
    <td align="right">14.63</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.82</td>
    <td align="right">4.49</td>
    <td align="right">4.80</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.32</td>
    <td align="right">3.05</td>
    <td align="right">2.98</td>
    <td align="right">11.83</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.45</td>
    <td align="right">4.27</td>
    <td align="right">4.07</td>
    <td align="right">14.42</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.82</td>
    <td align="right">4.61</td>
    <td align="right">4.48</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.53</td>
    <td align="right">5.33</td>
    <td align="right">13.79</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.63</td>
    <td align="right">8.14</td>
    <td align="right">7.96</td>
    <td align="right">17.47</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.80</td>
    <td align="right">7.93</td>
    <td align="right">7.93</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.57</td>
    <td align="right">5.58</td>
    <td align="right">5.34</td>
    <td align="right">13.86</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.49</td>
    <td align="right">8.66</td>
    <td align="right">8.59</td>
    <td align="right">17.71</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.63</td>
    <td align="right">8.72</td>
    <td align="right">8.75</td>
    <td align="right">18.54</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.91</td>
    <td align="right">3.04</td>
    <td align="right">3.41</td>
    <td align="right">11.85</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.44</td>
    <td align="right">4.49</td>
    <td align="right">4.80</td>
    <td align="right">14.65</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.63</td>
    <td align="right">4.30</td>
    <td align="right">4.61</td>
    <td align="right">14.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.03</td>
    <td align="right">3.13</td>
    <td align="right">3.02</td>
    <td align="right">11.95</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.47</td>
    <td align="right">4.18</td>
    <td align="right">3.99</td>
    <td align="right">14.10</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.58</td>
    <td align="right">4.42</td>
    <td align="right">4.35</td>
    <td align="right">14.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.46</td>
    <td align="right">5.61</td>
    <td align="right">3.69</td>
    <td align="right">14.37</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.32</td>
    <td align="right">8.00</td>
    <td align="right">5.76</td>
    <td align="right">17.69</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.46</td>
    <td align="right">7.84</td>
    <td align="right">5.82</td>
    <td align="right">17.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.52</td>
    <td align="right">5.66</td>
    <td align="right">3.65</td>
    <td align="right">14.51</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.00</td>
    <td align="right">9.14</td>
    <td align="right">5.95</td>
    <td align="right">18.93</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.71</td>
    <td align="right">8.91</td>
    <td align="right">5.91</td>
    <td align="right">18.02</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.95</td>
    <td align="right">3.04</td>
    <td align="right">3.42</td>
    <td align="right">11.50</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.47</td>
    <td align="right">4.51</td>
    <td align="right">4.84</td>
    <td align="right">14.65</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.64</td>
    <td align="right">4.30</td>
    <td align="right">4.58</td>
    <td align="right">14.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.02</td>
    <td align="right">3.10</td>
    <td align="right">3.00</td>
    <td align="right">11.68</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.41</td>
    <td align="right">4.20</td>
    <td align="right">3.96</td>
    <td align="right">14.34</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.58</td>
    <td align="right">4.43</td>
    <td align="right">4.25</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.47</td>
    <td align="right">5.33</td>
    <td align="right">5.16</td>
    <td align="right">13.66</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.35</td>
    <td align="right">7.67</td>
    <td align="right">7.14</td>
    <td align="right">16.55</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.44</td>
    <td align="right">7.46</td>
    <td align="right">7.05</td>
    <td align="right">16.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.52</td>
    <td align="right">5.37</td>
    <td align="right">5.18</td>
    <td align="right">13.81</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.96</td>
    <td align="right">8.31</td>
    <td align="right">7.97</td>
    <td align="right">16.99</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.71</td>
    <td align="right">7.99</td>
    <td align="right">8.13</td>
    <td align="right">16.31</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.42</td>
    <td align="right">7.25</td>
    <td align="right">14.89</td>
    <td align="right">13.24</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">8.61</td>
    <td align="right">19.11</td>
    <td align="right">15.94</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.34</td>
    <td align="right">11.09</td>
    <td align="right">20.05</td>
    <td align="right">16.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.14</td>
    <td align="right">14.54</td>
    <td align="right">17.37</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.55</td>
    <td align="right">10.31</td>
    <td align="right">16.28</td>
    <td align="right">17.23</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.07</td>
    <td align="right">14.37</td>
    <td align="right">20.52</td>
    <td align="right">19.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">11.49</td>
    <td align="right">13.86</td>
    <td align="right">16.69</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.98</td>
    <td align="right">12.74</td>
    <td align="right">17.32</td>
    <td align="right">19.49</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.45</td>
    <td align="right">15.60</td>
    <td align="right">18.99</td>
    <td align="right">19.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.88</td>
    <td align="right">14.17</td>
    <td align="right">15.11</td>
    <td align="right">18.12</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.65</td>
    <td align="right">15.00</td>
    <td align="right">16.86</td>
    <td align="right">20.09</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.68</td>
    <td align="right">20.73</td>
    <td align="right">21.55</td>
    <td align="right">23.10</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.44</td>
    <td align="right">7.11</td>
    <td align="right">7.33</td>
    <td align="right">13.45</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">8.84</td>
    <td align="right">8.98</td>
    <td align="right">16.10</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.24</td>
    <td align="right">11.37</td>
    <td align="right">11.27</td>
    <td align="right">18.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.05</td>
    <td align="right">10.01</td>
    <td align="right">16.48</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.57</td>
    <td align="right">11.04</td>
    <td align="right">10.98</td>
    <td align="right">18.05</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.22</td>
    <td align="right">14.81</td>
    <td align="right">14.01</td>
    <td align="right">21.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">11.31</td>
    <td align="right">11.26</td>
    <td align="right">17.57</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.97</td>
    <td align="right">13.94</td>
    <td align="right">13.21</td>
    <td align="right">20.58</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.35</td>
    <td align="right">16.61</td>
    <td align="right">16.17</td>
    <td align="right">22.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.87</td>
    <td align="right">14.27</td>
    <td align="right">14.13</td>
    <td align="right">20.06</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.66</td>
    <td align="right">16.06</td>
    <td align="right">15.98</td>
    <td align="right">21.70</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.58</td>
    <td align="right">20.83</td>
    <td align="right">20.90</td>
    <td align="right">26.21</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.41</td>
    <td align="right">7.24</td>
    <td align="right">14.94</td>
    <td align="right">13.27</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.20</td>
    <td align="right">8.51</td>
    <td align="right">18.71</td>
    <td align="right">16.13</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.04</td>
    <td align="right">10.53</td>
    <td align="right">19.36</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.10</td>
    <td align="right">10.26</td>
    <td align="right">14.32</td>
    <td align="right">16.37</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.59</td>
    <td align="right">10.17</td>
    <td align="right">16.05</td>
    <td align="right">17.28</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.70</td>
    <td align="right">13.32</td>
    <td align="right">19.50</td>
    <td align="right">18.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.11</td>
    <td align="right">11.62</td>
    <td align="right">13.83</td>
    <td align="right">17.02</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.36</td>
    <td align="right">12.75</td>
    <td align="right">17.03</td>
    <td align="right">19.38</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.13</td>
    <td align="right">15.48</td>
    <td align="right">17.04</td>
    <td align="right">19.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.28</td>
    <td align="right">14.29</td>
    <td align="right">14.89</td>
    <td align="right">18.58</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.63</td>
    <td align="right">14.85</td>
    <td align="right">16.54</td>
    <td align="right">20.39</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.17</td>
    <td align="right">21.05</td>
    <td align="right">18.20</td>
    <td align="right">23.11</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.40</td>
    <td align="right">7.22</td>
    <td align="right">7.32</td>
    <td align="right">13.56</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.23</td>
    <td align="right">8.80</td>
    <td align="right">8.90</td>
    <td align="right">15.98</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.02</td>
    <td align="right">10.80</td>
    <td align="right">11.01</td>
    <td align="right">17.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.08</td>
    <td align="right">10.07</td>
    <td align="right">10.05</td>
    <td align="right">16.56</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.62</td>
    <td align="right">10.97</td>
    <td align="right">10.90</td>
    <td align="right">17.73</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.78</td>
    <td align="right">14.28</td>
    <td align="right">14.21</td>
    <td align="right">20.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.09</td>
    <td align="right">11.42</td>
    <td align="right">11.60</td>
    <td align="right">17.88</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.36</td>
    <td align="right">13.97</td>
    <td align="right">13.19</td>
    <td align="right">20.47</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.16</td>
    <td align="right">16.00</td>
    <td align="right">15.68</td>
    <td align="right">22.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.27</td>
    <td align="right">14.40</td>
    <td align="right">14.34</td>
    <td align="right">20.03</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.65</td>
    <td align="right">15.93</td>
    <td align="right">15.90</td>
    <td align="right">21.75</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.21</td>
    <td align="right">20.05</td>
    <td align="right">19.91</td>
    <td align="right">25.94</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.13</td>
    <td align="right">25.56</td>
    <td align="right">14.42</td>
    <td align="right">32.39</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.04</td>
    <td align="right">16.66</td>
    <td align="right">21.30</td>
    <td align="right">20.60</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.50</td>
    <td align="right">5.76</td>
    <td align="right">6.00</td>
    <td align="right">12.70</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.28</td>
    <td align="right">5.62</td>
    <td align="right">6.48</td>
    <td align="right">12.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.67</td>
    <td align="right">51.68</td>
    <td align="right">27.61</td>
    <td align="right">41.11</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.41</td>
    <td align="right">10.85</td>
    <td align="right">10.79</td>
    <td align="right">16.71</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.86</td>
    <td align="right">12.84</td>
    <td align="right">12.52</td>
    <td align="right">17.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.46</td>
    <td align="right">92.25</td>
    <td align="right">33.28</td>
    <td align="right">65.49</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.72</td>
    <td align="right">18.17</td>
    <td align="right">17.65</td>
    <td align="right">23.26</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.89</td>
    <td align="right">18.68</td>
    <td align="right">18.60</td>
    <td align="right">23.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">123.30</td>
    <td align="right">133.08</td>
    <td align="right">39.03</td>
    <td align="right">90.70</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.73</td>
    <td align="right">21.63</td>
    <td align="right">21.50</td>
    <td align="right">26.74</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.68</td>
    <td align="right">25.07</td>
    <td align="right">22.36</td>
    <td align="right">28.89</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.69</td>
    <td align="right">17.33</td>
    <td align="right">16.08</td>
    <td align="right">22.82</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.91</td>
    <td align="right">5.13</td>
    <td align="right">5.47</td>
    <td align="right">12.26</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.48</td>
    <td align="right">5.84</td>
    <td align="right">6.74</td>
    <td align="right">12.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.84</td>
    <td align="right">51.31</td>
    <td align="right">43.45</td>
    <td align="right">53.22</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.94</td>
    <td align="right">11.37</td>
    <td align="right">11.32</td>
    <td align="right">17.12</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.99</td>
    <td align="right">12.57</td>
    <td align="right">12.21</td>
    <td align="right">17.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.90</td>
    <td align="right">84.60</td>
    <td align="right">71.61</td>
    <td align="right">86.08</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.58</td>
    <td align="right">18.08</td>
    <td align="right">17.56</td>
    <td align="right">23.17</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.76</td>
    <td align="right">18.63</td>
    <td align="right">18.54</td>
    <td align="right">23.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">128.23</td>
    <td align="right">134.15</td>
    <td align="right">106.23</td>
    <td align="right">126.19</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.89</td>
    <td align="right">21.90</td>
    <td align="right">21.79</td>
    <td align="right">27.07</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.70</td>
    <td align="right">25.05</td>
    <td align="right">22.36</td>
    <td align="right">28.87</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">12.72</td>
    <td align="right">15.19</td>
    <td align="right">22.65</td>
    <td align="right">19.40</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.17</td>
    <td align="right">5.45</td>
    <td align="right">5.78</td>
    <td align="right">12.26</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.41</td>
    <td align="right">6.83</td>
    <td align="right">6.86</td>
    <td align="right">13.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">44.73</td>
    <td align="right">51.76</td>
    <td align="right">29.16</td>
    <td align="right">40.78</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.55</td>
    <td align="right">11.42</td>
    <td align="right">10.83</td>
    <td align="right">16.72</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.46</td>
    <td align="right">12.71</td>
    <td align="right">12.75</td>
    <td align="right">18.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">77.67</td>
    <td align="right">92.78</td>
    <td align="right">35.77</td>
    <td align="right">65.50</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.83</td>
    <td align="right">18.00</td>
    <td align="right">17.82</td>
    <td align="right">23.12</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.96</td>
    <td align="right">21.00</td>
    <td align="right">18.86</td>
    <td align="right">24.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.23</td>
    <td align="right">137.16</td>
    <td align="right">43.22</td>
    <td align="right">93.00</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.70</td>
    <td align="right">24.52</td>
    <td align="right">21.58</td>
    <td align="right">27.64</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.20</td>
    <td align="right">25.23</td>
    <td align="right">25.01</td>
    <td align="right">30.11</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.37</td>
    <td align="right">18.17</td>
    <td align="right">16.31</td>
    <td align="right">24.06</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.08</td>
    <td align="right">5.36</td>
    <td align="right">5.69</td>
    <td align="right">12.23</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.20</td>
    <td align="right">6.63</td>
    <td align="right">6.69</td>
    <td align="right">12.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.82</td>
    <td align="right">59.13</td>
    <td align="right">44.31</td>
    <td align="right">59.39</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.51</td>
    <td align="right">11.38</td>
    <td align="right">10.77</td>
    <td align="right">16.81</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.62</td>
    <td align="right">11.84</td>
    <td align="right">11.72</td>
    <td align="right">17.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">80.37</td>
    <td align="right">119.54</td>
    <td align="right">79.40</td>
    <td align="right">115.77</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.85</td>
    <td align="right">18.06</td>
    <td align="right">17.87</td>
    <td align="right">23.24</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.81</td>
    <td align="right">20.77</td>
    <td align="right">18.67</td>
    <td align="right">24.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">114.64</td>
    <td align="right">160.18</td>
    <td align="right">118.46</td>
    <td align="right">171.88</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.18</td>
    <td align="right">24.56</td>
    <td align="right">21.66</td>
    <td align="right">27.66</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.28</td>
    <td align="right">25.33</td>
    <td align="right">25.14</td>
    <td align="right">30.42</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.29</td>
    <td align="right">6.76</td>
    <td align="right">15.27</td>
    <td align="right">13.92</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.03</td>
    <td align="right">9.10</td>
    <td align="right">17.03</td>
    <td align="right">15.23</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.16</td>
    <td align="right">4.14</td>
    <td align="right">4.70</td>
    <td align="right">13.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.79</td>
    <td align="right">15.27</td>
    <td align="right">19.37</td>
    <td align="right">20.11</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">17.38</td>
    <td align="right">19.67</td>
    <td align="right">24.17</td>
    <td align="right">24.40</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.64</td>
    <td align="right">8.35</td>
    <td align="right">7.96</td>
    <td align="right">15.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.34</td>
    <td align="right">30.97</td>
    <td align="right">24.51</td>
    <td align="right">30.97</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">36.09</td>
    <td align="right">32.85</td>
    <td align="right">28.35</td>
    <td align="right">34.60</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.13</td>
    <td align="right">21.23</td>
    <td align="right">14.97</td>
    <td align="right">26.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.29</td>
    <td align="right">40.45</td>
    <td align="right">27.36</td>
    <td align="right">40.59</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.76</td>
    <td align="right">42.98</td>
    <td align="right">32.32</td>
    <td align="right">44.85</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.06</td>
    <td align="right">24.44</td>
    <td align="right">16.78</td>
    <td align="right">29.32</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.57</td>
    <td align="right">7.60</td>
    <td align="right">7.81</td>
    <td align="right">14.72</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.11</td>
    <td align="right">9.70</td>
    <td align="right">9.65</td>
    <td align="right">16.50</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">5.43</td>
    <td align="right">5.53</td>
    <td align="right">5.84</td>
    <td align="right">13.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.53</td>
    <td align="right">14.85</td>
    <td align="right">14.76</td>
    <td align="right">20.79</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.32</td>
    <td align="right">19.86</td>
    <td align="right">18.73</td>
    <td align="right">25.61</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.81</td>
    <td align="right">8.59</td>
    <td align="right">8.21</td>
    <td align="right">15.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.89</td>
    <td align="right">31.21</td>
    <td align="right">30.83</td>
    <td align="right">35.55</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">36.00</td>
    <td align="right">34.40</td>
    <td align="right">34.31</td>
    <td align="right">39.81</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.27</td>
    <td align="right">20.98</td>
    <td align="right">20.44</td>
    <td align="right">26.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.44</td>
    <td align="right">39.83</td>
    <td align="right">39.35</td>
    <td align="right">44.65</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.95</td>
    <td align="right">50.71</td>
    <td align="right">50.18</td>
    <td align="right">56.28</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.01</td>
    <td align="right">24.11</td>
    <td align="right">23.46</td>
    <td align="right">30.23</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">5.77</td>
    <td align="right">6.85</td>
    <td align="right">15.52</td>
    <td align="right">14.12</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.41</td>
    <td align="right">9.40</td>
    <td align="right">16.88</td>
    <td align="right">15.25</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.60</td>
    <td align="right">4.08</td>
    <td align="right">4.58</td>
    <td align="right">13.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.19</td>
    <td align="right">14.95</td>
    <td align="right">18.98</td>
    <td align="right">19.41</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.76</td>
    <td align="right">18.52</td>
    <td align="right">23.04</td>
    <td align="right">22.53</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.71</td>
    <td align="right">8.84</td>
    <td align="right">8.66</td>
    <td align="right">15.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">28.54</td>
    <td align="right">30.17</td>
    <td align="right">23.55</td>
    <td align="right">29.80</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.31</td>
    <td align="right">32.13</td>
    <td align="right">26.48</td>
    <td align="right">33.62</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.56</td>
    <td align="right">20.86</td>
    <td align="right">14.69</td>
    <td align="right">25.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.26</td>
    <td align="right">40.10</td>
    <td align="right">24.76</td>
    <td align="right">39.59</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.02</td>
    <td align="right">42.34</td>
    <td align="right">31.10</td>
    <td align="right">43.97</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.34</td>
    <td align="right">23.94</td>
    <td align="right">16.33</td>
    <td align="right">27.39</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.18</td>
    <td align="right">7.51</td>
    <td align="right">7.62</td>
    <td align="right">14.14</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.94</td>
    <td align="right">8.89</td>
    <td align="right">8.88</td>
    <td align="right">15.90</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.70</td>
    <td align="right">4.21</td>
    <td align="right">4.76</td>
    <td align="right">14.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.97</td>
    <td align="right">14.36</td>
    <td align="right">14.34</td>
    <td align="right">20.30</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.65</td>
    <td align="right">19.74</td>
    <td align="right">18.76</td>
    <td align="right">25.85</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.61</td>
    <td align="right">8.96</td>
    <td align="right">8.51</td>
    <td align="right">15.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">28.88</td>
    <td align="right">30.85</td>
    <td align="right">30.67</td>
    <td align="right">35.88</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.49</td>
    <td align="right">32.82</td>
    <td align="right">32.63</td>
    <td align="right">38.30</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.49</td>
    <td align="right">20.71</td>
    <td align="right">18.89</td>
    <td align="right">26.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.20</td>
    <td align="right">38.83</td>
    <td align="right">38.67</td>
    <td align="right">43.78</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.02</td>
    <td align="right">49.97</td>
    <td align="right">49.49</td>
    <td align="right">55.71</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.35</td>
    <td align="right">23.65</td>
    <td align="right">21.30</td>
    <td align="right">29.51</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.44</td>
    <td align="right">4.38</td>
    <td align="right">4.80</td>
    <td align="right">12.64</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.07</td>
    <td align="right">6.38</td>
    <td align="right">6.62</td>
    <td align="right">16.15</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.04</td>
    <td align="right">5.98</td>
    <td align="right">6.19</td>
    <td align="right">15.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.42</td>
    <td align="right">8.76</td>
    <td align="right">8.31</td>
    <td align="right">15.01</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.05</td>
    <td align="right">10.40</td>
    <td align="right">9.94</td>
    <td align="right">18.22</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.73</td>
    <td align="right">11.78</td>
    <td align="right">11.50</td>
    <td align="right">18.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.90</td>
    <td align="right">21.08</td>
    <td align="right">14.84</td>
    <td align="right">26.44</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.37</td>
    <td align="right">26.69</td>
    <td align="right">21.85</td>
    <td align="right">31.50</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.14</td>
    <td align="right">26.91</td>
    <td align="right">21.93</td>
    <td align="right">31.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.77</td>
    <td align="right">24.30</td>
    <td align="right">16.59</td>
    <td align="right">27.53</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.27</td>
    <td align="right">36.76</td>
    <td align="right">25.04</td>
    <td align="right">37.75</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.43</td>
    <td align="right">36.80</td>
    <td align="right">25.23</td>
    <td align="right">37.61</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.69</td>
    <td align="right">4.64</td>
    <td align="right">5.03</td>
    <td align="right">12.81</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.07</td>
    <td align="right">6.31</td>
    <td align="right">6.63</td>
    <td align="right">16.14</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.50</td>
    <td align="right">6.48</td>
    <td align="right">6.68</td>
    <td align="right">15.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.75</td>
    <td align="right">9.11</td>
    <td align="right">8.70</td>
    <td align="right">15.37</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.99</td>
    <td align="right">10.16</td>
    <td align="right">9.87</td>
    <td align="right">18.30</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">12.15</td>
    <td align="right">13.31</td>
    <td align="right">12.46</td>
    <td align="right">19.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.83</td>
    <td align="right">20.71</td>
    <td align="right">20.21</td>
    <td align="right">25.74</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.20</td>
    <td align="right">26.33</td>
    <td align="right">26.47</td>
    <td align="right">33.07</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.24</td>
    <td align="right">27.12</td>
    <td align="right">26.65</td>
    <td align="right">32.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.88</td>
    <td align="right">24.09</td>
    <td align="right">23.48</td>
    <td align="right">29.69</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.19</td>
    <td align="right">35.59</td>
    <td align="right">31.81</td>
    <td align="right">38.58</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.27</td>
    <td align="right">36.11</td>
    <td align="right">31.93</td>
    <td align="right">38.77</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.68</td>
    <td align="right">4.05</td>
    <td align="right">4.56</td>
    <td align="right">13.43</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.90</td>
    <td align="right">6.09</td>
    <td align="right">6.39</td>
    <td align="right">16.30</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.54</td>
    <td align="right">5.30</td>
    <td align="right">5.67</td>
    <td align="right">15.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.74</td>
    <td align="right">8.93</td>
    <td align="right">8.53</td>
    <td align="right">15.65</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.30</td>
    <td align="right">10.41</td>
    <td align="right">10.13</td>
    <td align="right">18.25</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.97</td>
    <td align="right">12.22</td>
    <td align="right">11.82</td>
    <td align="right">18.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.43</td>
    <td align="right">20.66</td>
    <td align="right">14.46</td>
    <td align="right">24.40</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.21</td>
    <td align="right">25.93</td>
    <td align="right">19.63</td>
    <td align="right">29.84</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.74</td>
    <td align="right">26.08</td>
    <td align="right">19.65</td>
    <td align="right">29.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.35</td>
    <td align="right">23.74</td>
    <td align="right">16.07</td>
    <td align="right">27.21</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.05</td>
    <td align="right">35.89</td>
    <td align="right">22.78</td>
    <td align="right">36.52</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.30</td>
    <td align="right">32.05</td>
    <td align="right">22.86</td>
    <td align="right">35.87</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.97</td>
    <td align="right">4.42</td>
    <td align="right">4.98</td>
    <td align="right">13.71</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.62</td>
    <td align="right">6.94</td>
    <td align="right">7.14</td>
    <td align="right">16.62</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.53</td>
    <td align="right">6.55</td>
    <td align="right">6.70</td>
    <td align="right">15.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.72</td>
    <td align="right">8.93</td>
    <td align="right">8.53</td>
    <td align="right">16.83</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.39</td>
    <td align="right">10.54</td>
    <td align="right">10.20</td>
    <td align="right">18.52</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.85</td>
    <td align="right">12.11</td>
    <td align="right">11.65</td>
    <td align="right">18.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.38</td>
    <td align="right">20.36</td>
    <td align="right">18.48</td>
    <td align="right">25.07</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.39</td>
    <td align="right">25.87</td>
    <td align="right">25.48</td>
    <td align="right">31.86</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.89</td>
    <td align="right">25.99</td>
    <td align="right">25.62</td>
    <td align="right">31.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.27</td>
    <td align="right">23.55</td>
    <td align="right">21.09</td>
    <td align="right">28.65</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.92</td>
    <td align="right">31.50</td>
    <td align="right">31.38</td>
    <td align="right">36.94</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.15</td>
    <td align="right">31.63</td>
    <td align="right">31.53</td>
    <td align="right">36.64</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.00</td>
    <td align="right">8.83</td>
    <td align="right">16.12</td>
    <td align="right">14.97</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.68</td>
    <td align="right">10.27</td>
    <td align="right">20.80</td>
    <td align="right">18.07</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.43</td>
    <td align="right">15.61</td>
    <td align="right">24.57</td>
    <td align="right">21.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.36</td>
    <td align="right">17.53</td>
    <td align="right">18.62</td>
    <td align="right">22.35</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.70</td>
    <td align="right">20.63</td>
    <td align="right">20.76</td>
    <td align="right">25.23</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.76</td>
    <td align="right">30.18</td>
    <td align="right">26.85</td>
    <td align="right">29.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.91</td>
    <td align="right">28.16</td>
    <td align="right">21.89</td>
    <td align="right">31.10</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.16</td>
    <td align="right">33.60</td>
    <td align="right">26.48</td>
    <td align="right">37.08</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.78</td>
    <td align="right">47.27</td>
    <td align="right">32.53</td>
    <td align="right">41.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.97</td>
    <td align="right">42.76</td>
    <td align="right">25.52</td>
    <td align="right">42.94</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.20</td>
    <td align="right">50.54</td>
    <td align="right">28.93</td>
    <td align="right">48.91</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.23</td>
    <td align="right">70.09</td>
    <td align="right">39.40</td>
    <td align="right">59.24</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.08</td>
    <td align="right">8.87</td>
    <td align="right">9.07</td>
    <td align="right">15.71</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.33</td>
    <td align="right">11.55</td>
    <td align="right">11.62</td>
    <td align="right">19.32</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.03</td>
    <td align="right">14.48</td>
    <td align="right">14.66</td>
    <td align="right">20.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.91</td>
    <td align="right">19.14</td>
    <td align="right">19.03</td>
    <td align="right">25.29</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.20</td>
    <td align="right">22.66</td>
    <td align="right">22.58</td>
    <td align="right">28.86</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.90</td>
    <td align="right">31.67</td>
    <td align="right">31.57</td>
    <td align="right">37.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.45</td>
    <td align="right">30.82</td>
    <td align="right">27.63</td>
    <td align="right">33.82</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.26</td>
    <td align="right">41.16</td>
    <td align="right">40.33</td>
    <td align="right">46.83</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.90</td>
    <td align="right">50.67</td>
    <td align="right">49.92</td>
    <td align="right">55.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.77</td>
    <td align="right">43.22</td>
    <td align="right">42.94</td>
    <td align="right">48.33</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.09</td>
    <td align="right">51.68</td>
    <td align="right">51.36</td>
    <td align="right">56.70</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.59</td>
    <td align="right">74.67</td>
    <td align="right">74.34</td>
    <td align="right">79.21</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.54</td>
    <td align="right">9.37</td>
    <td align="right">16.51</td>
    <td align="right">15.37</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.11</td>
    <td align="right">9.96</td>
    <td align="right">20.09</td>
    <td align="right">18.17</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.90</td>
    <td align="right">14.98</td>
    <td align="right">22.38</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.22</td>
    <td align="right">17.95</td>
    <td align="right">18.60</td>
    <td align="right">22.93</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.61</td>
    <td align="right">20.12</td>
    <td align="right">20.24</td>
    <td align="right">24.76</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">27.33</td>
    <td align="right">27.96</td>
    <td align="right">24.92</td>
    <td align="right">29.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.01</td>
    <td align="right">27.95</td>
    <td align="right">21.73</td>
    <td align="right">31.42</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.54</td>
    <td align="right">33.56</td>
    <td align="right">25.98</td>
    <td align="right">37.11</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.88</td>
    <td align="right">46.60</td>
    <td align="right">23.22</td>
    <td align="right">41.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.18</td>
    <td align="right">42.45</td>
    <td align="right">24.96</td>
    <td align="right">42.83</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.29</td>
    <td align="right">50.73</td>
    <td align="right">28.12</td>
    <td align="right">49.07</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">75.03</td>
    <td align="right">67.21</td>
    <td align="right">27.16</td>
    <td align="right">55.07</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.09</td>
    <td align="right">9.00</td>
    <td align="right">9.09</td>
    <td align="right">15.80</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.09</td>
    <td align="right">10.92</td>
    <td align="right">10.80</td>
    <td align="right">18.49</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.90</td>
    <td align="right">13.65</td>
    <td align="right">13.82</td>
    <td align="right">20.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.38</td>
    <td align="right">18.32</td>
    <td align="right">18.34</td>
    <td align="right">24.54</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.72</td>
    <td align="right">21.92</td>
    <td align="right">21.76</td>
    <td align="right">28.06</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.59</td>
    <td align="right">30.62</td>
    <td align="right">30.30</td>
    <td align="right">36.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.01</td>
    <td align="right">31.37</td>
    <td align="right">31.20</td>
    <td align="right">37.38</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.91</td>
    <td align="right">41.48</td>
    <td align="right">40.72</td>
    <td align="right">47.08</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.38</td>
    <td align="right">50.41</td>
    <td align="right">49.43</td>
    <td align="right">54.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.45</td>
    <td align="right">43.37</td>
    <td align="right">43.29</td>
    <td align="right">48.49</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.85</td>
    <td align="right">51.33</td>
    <td align="right">51.26</td>
    <td align="right">56.43</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.89</td>
    <td align="right">74.85</td>
    <td align="right">74.46</td>
    <td align="right">79.74</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.32</td>
    <td align="right">5.96</td>
    <td align="right">3.91</td>
    <td align="right">12.90</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.35</td>
    <td align="right">11.72</td>
    <td align="right">17.58</td>
    <td align="right">16.67</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.07</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.08</td>
    <td align="right">4.93</td>
    <td align="right">4.94</td>
    <td align="right">4.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.76</td>
    <td align="right">17.17</td>
    <td align="right">18.51</td>
    <td align="right">20.29</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">5.34</td>
    <td align="right">5.33</td>
    <td align="right">5.33</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.49</td>
    <td align="right">5.50</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.82</td>
    <td align="right">20.49</td>
    <td align="right">17.29</td>
    <td align="right">22.78</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.93</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.56</td>
    <td align="right">24.76</td>
    <td align="right">17.67</td>
    <td align="right">25.21</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.75</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.31</td>
    <td align="right">11.01</td>
    <td align="right">11.00</td>
    <td align="right">11.00</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.05</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.92</td>
    <td align="right">4.92</td>
    <td align="right">4.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.66</td>
    <td align="right">15.18</td>
    <td align="right">15.18</td>
    <td align="right">15.22</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.58</td>
    <td align="right">5.33</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.50</td>
    <td align="right">5.50</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.78</td>
    <td align="right">18.22</td>
    <td align="right">18.27</td>
    <td align="right">18.21</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.75</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.94</td>
    <td align="right">5.92</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.34</td>
    <td align="right">25.20</td>
    <td align="right">25.01</td>
    <td align="right">25.01</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.32</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.41</td>
    <td align="right">11.22</td>
    <td align="right">18.38</td>
    <td align="right">16.11</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.49</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.27</td>
    <td align="right">15.93</td>
    <td align="right">19.59</td>
    <td align="right">19.73</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.02</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.47</td>
    <td align="right">5.42</td>
    <td align="right">5.43</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.34</td>
    <td align="right">19.10</td>
    <td align="right">18.82</td>
    <td align="right">21.68</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.43</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.90</td>
    <td align="right">5.84</td>
    <td align="right">5.84</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.87</td>
    <td align="right">23.59</td>
    <td align="right">19.23</td>
    <td align="right">24.31</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.84</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.26</td>
    <td align="right">3.63</td>
    <td align="right">3.64</td>
    <td align="right">3.64</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.42</td>
    <td align="right">10.51</td>
    <td align="right">10.55</td>
    <td align="right">10.62</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.50</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.03</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.30</td>
    <td align="right">14.26</td>
    <td align="right">14.26</td>
    <td align="right">14.25</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.02</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.49</td>
    <td align="right">5.43</td>
    <td align="right">5.41</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.84</td>
    <td align="right">16.93</td>
    <td align="right">16.98</td>
    <td align="right">16.93</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.43</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="right">5.71</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.89</td>
    <td align="right">5.83</td>
    <td align="right">5.83</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.77</td>
    <td align="right">24.64</td>
    <td align="right">24.64</td>
    <td align="right">24.64</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.84</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.24</td>
    <td align="right">3.64</td>
    <td align="right">3.65</td>
    <td align="right">3.64</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.23</td>
    <td align="right">6.35</td>
    <td align="right">13.73</td>
    <td align="right">12.21</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.31</td>
    <td align="right">6.31</td>
    <td align="right">13.36</td>
    <td align="right">11.84</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">3.35</td>
    <td align="right">3.37</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.36</td>
    <td align="right">8.87</td>
    <td align="right">14.33</td>
    <td align="right">13.60</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.04</td>
    <td align="right">8.91</td>
    <td align="right">14.49</td>
    <td align="right">14.04</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.79</td>
    <td align="right">3.19</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.83</td>
    <td align="right">12.18</td>
    <td align="right">16.35</td>
    <td align="right">17.21</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.99</td>
    <td align="right">11.76</td>
    <td align="right">15.12</td>
    <td align="right">16.25</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.41</td>
    <td align="right">4.57</td>
    <td align="right">2.95</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.22</td>
    <td align="right">13.51</td>
    <td align="right">15.23</td>
    <td align="right">18.25</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.94</td>
    <td align="right">13.54</td>
    <td align="right">15.77</td>
    <td align="right">17.99</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.42</td>
    <td align="right">4.61</td>
    <td align="right">2.94</td>
    <td align="right">13.82</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.23</td>
    <td align="right">6.31</td>
    <td align="right">6.31</td>
    <td align="right">6.31</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.35</td>
    <td align="right">6.22</td>
    <td align="right">6.22</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.39</td>
    <td align="right">5.34</td>
    <td align="right">5.34</td>
    <td align="right">5.34</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.02</td>
    <td align="right">5.50</td>
    <td align="right">5.47</td>
    <td align="right">5.48</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.78</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.81</td>
    <td align="right">8.11</td>
    <td align="right">8.12</td>
    <td align="right">8.10</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.98</td>
    <td align="right">7.92</td>
    <td align="right">7.92</td>
    <td align="right">7.89</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.41</td>
    <td align="right">4.83</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.20</td>
    <td align="right">8.67</td>
    <td align="right">8.66</td>
    <td align="right">8.67</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.96</td>
    <td align="right">8.93</td>
    <td align="right">8.93</td>
    <td align="right">8.94</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.44</td>
    <td align="right">4.86</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.13</td>
    <td align="right">6.31</td>
    <td align="right">13.67</td>
    <td align="right">11.82</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.15</td>
    <td align="right">6.12</td>
    <td align="right">13.18</td>
    <td align="right">11.49</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.66</td>
    <td align="right">3.34</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.97</td>
    <td align="right">8.71</td>
    <td align="right">14.36</td>
    <td align="right">13.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.84</td>
    <td align="right">8.75</td>
    <td align="right">14.35</td>
    <td align="right">14.02</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.23</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.37</td>
    <td align="right">11.97</td>
    <td align="right">15.48</td>
    <td align="right">16.45</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.58</td>
    <td align="right">11.71</td>
    <td align="right">14.78</td>
    <td align="right">16.28</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.21</td>
    <td align="right">4.16</td>
    <td align="right">2.71</td>
    <td align="right">13.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.82</td>
    <td align="right">13.44</td>
    <td align="right">15.39</td>
    <td align="right">17.69</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.79</td>
    <td align="right">13.68</td>
    <td align="right">15.22</td>
    <td align="right">18.38</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.28</td>
    <td align="right">4.19</td>
    <td align="right">2.67</td>
    <td align="right">13.61</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.11</td>
    <td align="right">6.21</td>
    <td align="right">6.21</td>
    <td align="right">6.21</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.16</td>
    <td align="right">6.10</td>
    <td align="right">6.10</td>
    <td align="right">6.10</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.63</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.94</td>
    <td align="right">5.29</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.89</td>
    <td align="right">5.32</td>
    <td align="right">5.31</td>
    <td align="right">5.35</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.22</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.34</td>
    <td align="right">7.75</td>
    <td align="right">7.74</td>
    <td align="right">7.74</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.57</td>
    <td align="right">7.64</td>
    <td align="right">7.64</td>
    <td align="right">7.65</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.25</td>
    <td align="right">4.82</td>
    <td align="right">4.83</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.85</td>
    <td align="right">8.37</td>
    <td align="right">8.28</td>
    <td align="right">8.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.81</td>
    <td align="right">8.59</td>
    <td align="right">8.62</td>
    <td align="right">8.62</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.28</td>
    <td align="right">4.85</td>
    <td align="right">4.86</td>
    <td align="right">4.84</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.85</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.91</td>
    <td align="right">4.43</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.97</td>
    <td align="right">3.20</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.25</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.45</td>
    <td align="right">4.32</td>
    <td align="right">2.75</td>
    <td align="right">13.19</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.81</td>
    <td align="right">6.48</td>
    <td align="right">4.78</td>
    <td align="right">16.73</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.01</td>
    <td align="right">6.00</td>
    <td align="right">4.36</td>
    <td align="right">16.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.50</td>
    <td align="right">4.35</td>
    <td align="right">2.73</td>
    <td align="right">13.26</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.86</td>
    <td align="right">7.01</td>
    <td align="right">4.83</td>
    <td align="right">17.36</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.22</td>
    <td align="right">6.93</td>
    <td align="right">4.67</td>
    <td align="right">16.74</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.84</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.91</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.07</td>
    <td align="right">4.21</td>
    <td align="right">4.21</td>
    <td align="right">4.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">3.19</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">4.26</td>
    <td align="right">4.26</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.23</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.44</td>
    <td align="right">4.55</td>
    <td align="right">4.56</td>
    <td align="right">4.55</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.78</td>
    <td align="right">6.67</td>
    <td align="right">6.67</td>
    <td align="right">6.67</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.01</td>
    <td align="right">6.50</td>
    <td align="right">6.49</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.91</td>
    <td align="right">7.83</td>
    <td align="right">7.82</td>
    <td align="right">7.83</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.22</td>
    <td align="right">7.59</td>
    <td align="right">7.65</td>
    <td align="right">7.65</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.62</td>
    <td align="right">3.03</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.65</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.87</td>
    <td align="right">4.03</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.78</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.17</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.08</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.42</td>
    <td align="right">4.19</td>
    <td align="right">2.61</td>
    <td align="right">13.32</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.50</td>
    <td align="right">5.69</td>
    <td align="right">3.86</td>
    <td align="right">16.16</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.87</td>
    <td align="right">5.55</td>
    <td align="right">3.68</td>
    <td align="right">16.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.46</td>
    <td align="right">4.22</td>
    <td align="right">2.53</td>
    <td align="right">13.38</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.75</td>
    <td align="right">7.03</td>
    <td align="right">3.84</td>
    <td align="right">16.99</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.14</td>
    <td align="right">6.84</td>
    <td align="right">3.73</td>
    <td align="right">16.73</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.67</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
    <td align="right">3.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.68</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.91</td>
    <td align="right">4.03</td>
    <td align="right">4.02</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.72</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.17</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.06</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.43</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.51</td>
    <td align="right">6.21</td>
    <td align="right">6.21</td>
    <td align="right">6.17</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.87</td>
    <td align="right">6.29</td>
    <td align="right">6.30</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.48</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.74</td>
    <td align="right">7.52</td>
    <td align="right">7.56</td>
    <td align="right">7.57</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.19</td>
    <td align="right">7.40</td>
    <td align="right">7.39</td>
    <td align="right">7.40</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.33</td>
    <td align="right">7.44</td>
    <td align="right">14.02</td>
    <td align="right">13.07</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">7.85</td>
    <td align="right">17.88</td>
    <td align="right">14.87</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.33</td>
    <td align="right">11.03</td>
    <td align="right">18.81</td>
    <td align="right">16.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.72</td>
    <td align="right">9.80</td>
    <td align="right">13.45</td>
    <td align="right">15.63</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">10.00</td>
    <td align="right">14.93</td>
    <td align="right">16.32</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.89</td>
    <td align="right">14.19</td>
    <td align="right">20.32</td>
    <td align="right">19.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">12.00</td>
    <td align="right">11.46</td>
    <td align="right">13.71</td>
    <td align="right">16.29</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.49</td>
    <td align="right">12.43</td>
    <td align="right">16.25</td>
    <td align="right">18.61</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.65</td>
    <td align="right">15.17</td>
    <td align="right">18.88</td>
    <td align="right">19.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.34</td>
    <td align="right">13.46</td>
    <td align="right">14.23</td>
    <td align="right">18.12</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.15</td>
    <td align="right">13.63</td>
    <td align="right">15.82</td>
    <td align="right">19.64</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.55</td>
    <td align="right">20.73</td>
    <td align="right">23.01</td>
    <td align="right">23.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.35</td>
    <td align="right">7.43</td>
    <td align="right">7.43</td>
    <td align="right">7.43</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.87</td>
    <td align="right">8.88</td>
    <td align="right">8.88</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.45</td>
    <td align="right">11.60</td>
    <td align="right">11.62</td>
    <td align="right">11.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.62</td>
    <td align="right">10.08</td>
    <td align="right">10.10</td>
    <td align="right">10.09</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.56</td>
    <td align="right">10.64</td>
    <td align="right">10.64</td>
    <td align="right">10.65</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.93</td>
    <td align="right">15.96</td>
    <td align="right">15.90</td>
    <td align="right">15.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.99</td>
    <td align="right">11.81</td>
    <td align="right">11.81</td>
    <td align="right">11.81</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.15</td>
    <td align="right">13.25</td>
    <td align="right">13.26</td>
    <td align="right">13.26</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.56</td>
    <td align="right">16.33</td>
    <td align="right">16.34</td>
    <td align="right">16.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.33</td>
    <td align="right">14.28</td>
    <td align="right">14.28</td>
    <td align="right">14.28</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.16</td>
    <td align="right">15.62</td>
    <td align="right">15.62</td>
    <td align="right">15.63</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.63</td>
    <td align="right">21.52</td>
    <td align="right">21.39</td>
    <td align="right">21.35</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">5.99</td>
    <td align="right">7.50</td>
    <td align="right">14.01</td>
    <td align="right">13.01</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">7.82</td>
    <td align="right">17.72</td>
    <td align="right">14.96</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.28</td>
    <td align="right">10.39</td>
    <td align="right">18.21</td>
    <td align="right">15.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.17</td>
    <td align="right">10.09</td>
    <td align="right">13.73</td>
    <td align="right">15.51</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.72</td>
    <td align="right">10.04</td>
    <td align="right">14.84</td>
    <td align="right">16.34</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.37</td>
    <td align="right">14.10</td>
    <td align="right">19.46</td>
    <td align="right">18.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.02</td>
    <td align="right">11.65</td>
    <td align="right">13.47</td>
    <td align="right">16.93</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.49</td>
    <td align="right">12.41</td>
    <td align="right">15.98</td>
    <td align="right">18.74</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.98</td>
    <td align="right">15.30</td>
    <td align="right">16.89</td>
    <td align="right">19.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.34</td>
    <td align="right">13.93</td>
    <td align="right">14.31</td>
    <td align="right">18.13</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.80</td>
    <td align="right">13.40</td>
    <td align="right">15.59</td>
    <td align="right">19.32</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.84</td>
    <td align="right">21.62</td>
    <td align="right">20.06</td>
    <td align="right">23.57</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">5.97</td>
    <td align="right">7.54</td>
    <td align="right">7.54</td>
    <td align="right">7.52</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">8.77</td>
    <td align="right">8.78</td>
    <td align="right">8.80</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.32</td>
    <td align="right">11.27</td>
    <td align="right">11.08</td>
    <td align="right">11.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.03</td>
    <td align="right">10.29</td>
    <td align="right">10.27</td>
    <td align="right">10.28</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">14.72</td>
    <td align="right">10.56</td>
    <td align="right">10.57</td>
    <td align="right">10.56</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.43</td>
    <td align="right">14.97</td>
    <td align="right">14.97</td>
    <td align="right">14.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.01</td>
    <td align="right">11.93</td>
    <td align="right">11.93</td>
    <td align="right">11.92</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.65</td>
    <td align="right">13.41</td>
    <td align="right">13.42</td>
    <td align="right">13.42</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.80</td>
    <td align="right">17.11</td>
    <td align="right">17.13</td>
    <td align="right">17.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.35</td>
    <td align="right">14.49</td>
    <td align="right">14.50</td>
    <td align="right">14.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.14</td>
    <td align="right">15.49</td>
    <td align="right">15.48</td>
    <td align="right">15.48</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.60</td>
    <td align="right">22.79</td>
    <td align="right">22.35</td>
    <td align="right">22.47</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.25</td>
    <td align="right">23.69</td>
    <td align="right">13.17</td>
    <td align="right">30.54</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.64</td>
    <td align="right">16.16</td>
    <td align="right">20.30</td>
    <td align="right">19.76</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.60</td>
    <td align="right">6.12</td>
    <td align="right">6.17</td>
    <td align="right">6.15</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.11</td>
    <td align="right">6.06</td>
    <td align="right">6.06</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.55</td>
    <td align="right">49.78</td>
    <td align="right">25.34</td>
    <td align="right">38.13</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.57</td>
    <td align="right">11.58</td>
    <td align="right">11.58</td>
    <td align="right">11.57</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.22</td>
    <td align="right">12.49</td>
    <td align="right">12.47</td>
    <td align="right">12.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.92</td>
    <td align="right">86.70</td>
    <td align="right">29.98</td>
    <td align="right">62.05</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.04</td>
    <td align="right">18.60</td>
    <td align="right">18.52</td>
    <td align="right">18.53</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.02</td>
    <td align="right">18.94</td>
    <td align="right">18.95</td>
    <td align="right">18.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.66</td>
    <td align="right">119.85</td>
    <td align="right">34.56</td>
    <td align="right">82.01</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.04</td>
    <td align="right">25.01</td>
    <td align="right">25.09</td>
    <td align="right">25.00</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.75</td>
    <td align="right">16.81</td>
    <td align="right">16.80</td>
    <td align="right">16.80</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.53</td>
    <td align="right">14.45</td>
    <td align="right">14.40</td>
    <td align="right">14.45</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.65</td>
    <td align="right">6.17</td>
    <td align="right">6.21</td>
    <td align="right">6.14</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.24</td>
    <td align="right">6.12</td>
    <td align="right">6.11</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.73</td>
    <td align="right">42.77</td>
    <td align="right">42.79</td>
    <td align="right">42.81</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.51</td>
    <td align="right">12.62</td>
    <td align="right">12.60</td>
    <td align="right">12.58</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.36</td>
    <td align="right">12.64</td>
    <td align="right">12.64</td>
    <td align="right">12.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.99</td>
    <td align="right">70.46</td>
    <td align="right">70.50</td>
    <td align="right">70.41</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.10</td>
    <td align="right">18.58</td>
    <td align="right">18.60</td>
    <td align="right">18.57</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.11</td>
    <td align="right">19.04</td>
    <td align="right">19.04</td>
    <td align="right">19.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.41</td>
    <td align="right">107.53</td>
    <td align="right">107.51</td>
    <td align="right">109.92</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.04</td>
    <td align="right">25.02</td>
    <td align="right">25.05</td>
    <td align="right">25.04</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.75</td>
    <td align="right">16.80</td>
    <td align="right">16.79</td>
    <td align="right">16.80</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">17.06</td>
    <td align="right">17.79</td>
    <td align="right">21.72</td>
    <td align="right">20.37</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.45</td>
    <td align="right">6.68</td>
    <td align="right">6.74</td>
    <td align="right">6.66</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.07</td>
    <td align="right">5.95</td>
    <td align="right">5.96</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.50</td>
    <td align="right">47.74</td>
    <td align="right">26.28</td>
    <td align="right">37.33</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.06</td>
    <td align="right">12.49</td>
    <td align="right">12.44</td>
    <td align="right">12.46</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.44</td>
    <td align="right">12.67</td>
    <td align="right">12.67</td>
    <td align="right">12.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.36</td>
    <td align="right">84.96</td>
    <td align="right">31.46</td>
    <td align="right">59.67</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.46</td>
    <td align="right">18.36</td>
    <td align="right">18.38</td>
    <td align="right">18.38</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.40</td>
    <td align="right">20.64</td>
    <td align="right">20.63</td>
    <td align="right">20.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">121.77</td>
    <td align="right">118.12</td>
    <td align="right">36.41</td>
    <td align="right">82.44</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.37</td>
    <td align="right">24.85</td>
    <td align="right">24.87</td>
    <td align="right">24.86</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.13</td>
    <td align="right">16.19</td>
    <td align="right">16.19</td>
    <td align="right">16.19</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.15</td>
    <td align="right">15.20</td>
    <td align="right">15.26</td>
    <td align="right">15.21</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.18</td>
    <td align="right">6.40</td>
    <td align="right">6.37</td>
    <td align="right">6.42</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.23</td>
    <td align="right">6.09</td>
    <td align="right">6.05</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">41.28</td>
    <td align="right">35.29</td>
    <td align="right">35.25</td>
    <td align="right">35.23</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">9.45</td>
    <td align="right">10.89</td>
    <td align="right">10.98</td>
    <td align="right">10.88</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.35</td>
    <td align="right">12.52</td>
    <td align="right">12.49</td>
    <td align="right">12.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.47</td>
    <td align="right">70.09</td>
    <td align="right">70.14</td>
    <td align="right">70.12</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.52</td>
    <td align="right">18.43</td>
    <td align="right">20.11</td>
    <td align="right">20.07</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.24</td>
    <td align="right">20.42</td>
    <td align="right">20.43</td>
    <td align="right">20.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">123.58</td>
    <td align="right">112.88</td>
    <td align="right">115.56</td>
    <td align="right">116.05</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.50</td>
    <td align="right">25.01</td>
    <td align="right">25.03</td>
    <td align="right">25.05</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.16</td>
    <td align="right">16.24</td>
    <td align="right">16.24</td>
    <td align="right">16.24</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.61</td>
    <td align="right">8.26</td>
    <td align="right">14.70</td>
    <td align="right">14.20</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.09</td>
    <td align="right">7.59</td>
    <td align="right">14.25</td>
    <td align="right">13.64</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.36</td>
    <td align="right">5.12</td>
    <td align="right">5.11</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.65</td>
    <td align="right">15.74</td>
    <td align="right">18.24</td>
    <td align="right">19.70</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.58</td>
    <td align="right">18.00</td>
    <td align="right">18.08</td>
    <td align="right">20.57</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.92</td>
    <td align="right">8.76</td>
    <td align="right">8.74</td>
    <td align="right">8.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.44</td>
    <td align="right">30.40</td>
    <td align="right">24.50</td>
    <td align="right">31.48</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.70</td>
    <td align="right">30.39</td>
    <td align="right">22.86</td>
    <td align="right">30.27</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.04</td>
    <td align="right">16.20</td>
    <td align="right">10.86</td>
    <td align="right">20.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.02</td>
    <td align="right">40.32</td>
    <td align="right">26.49</td>
    <td align="right">40.55</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">25.03</td>
    <td align="right">41.18</td>
    <td align="right">26.80</td>
    <td align="right">40.89</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.41</td>
    <td align="right">18.40</td>
    <td align="right">12.24</td>
    <td align="right">24.26</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.47</td>
    <td align="right">8.23</td>
    <td align="right">8.23</td>
    <td align="right">8.23</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.90</td>
    <td align="right">8.53</td>
    <td align="right">8.52</td>
    <td align="right">8.47</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.69</td>
    <td align="right">4.38</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.97</td>
    <td align="right">11.54</td>
    <td align="right">11.48</td>
    <td align="right">11.48</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.44</td>
    <td align="right">12.92</td>
    <td align="right">12.90</td>
    <td align="right">12.90</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.38</td>
    <td align="right">9.30</td>
    <td align="right">9.28</td>
    <td align="right">9.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.62</td>
    <td align="right">24.60</td>
    <td align="right">24.58</td>
    <td align="right">24.58</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.02</td>
    <td align="right">25.23</td>
    <td align="right">25.22</td>
    <td align="right">25.24</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.18</td>
    <td align="right">16.54</td>
    <td align="right">16.54</td>
    <td align="right">16.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.00</td>
    <td align="right">30.89</td>
    <td align="right">30.88</td>
    <td align="right">30.91</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">25.00</td>
    <td align="right">31.81</td>
    <td align="right">31.81</td>
    <td align="right">31.83</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.44</td>
    <td align="right">18.64</td>
    <td align="right">18.66</td>
    <td align="right">18.65</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">3.86</td>
    <td align="right">7.47</td>
    <td align="right">14.66</td>
    <td align="right">13.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.28</td>
    <td align="right">7.88</td>
    <td align="right">14.51</td>
    <td align="right">13.65</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.83</td>
    <td align="right">4.90</td>
    <td align="right">4.90</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.07</td>
    <td align="right">15.94</td>
    <td align="right">18.51</td>
    <td align="right">20.22</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.78</td>
    <td align="right">17.40</td>
    <td align="right">18.24</td>
    <td align="right">20.27</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.68</td>
    <td align="right">8.46</td>
    <td align="right">8.49</td>
    <td align="right">8.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.43</td>
    <td align="right">29.90</td>
    <td align="right">23.22</td>
    <td align="right">29.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.06</td>
    <td align="right">30.16</td>
    <td align="right">22.19</td>
    <td align="right">29.93</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.65</td>
    <td align="right">15.73</td>
    <td align="right">10.20</td>
    <td align="right">20.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.40</td>
    <td align="right">40.81</td>
    <td align="right">25.54</td>
    <td align="right">39.76</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.72</td>
    <td align="right">41.48</td>
    <td align="right">25.41</td>
    <td align="right">40.70</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.20</td>
    <td align="right">17.95</td>
    <td align="right">11.36</td>
    <td align="right">22.91</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.79</td>
    <td align="right">8.57</td>
    <td align="right">8.56</td>
    <td align="right">8.53</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.12</td>
    <td align="right">7.77</td>
    <td align="right">7.79</td>
    <td align="right">7.79</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.64</td>
    <td align="right">4.72</td>
    <td align="right">4.72</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.07</td>
    <td align="right">11.23</td>
    <td align="right">11.24</td>
    <td align="right">11.27</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.85</td>
    <td align="right">12.22</td>
    <td align="right">12.27</td>
    <td align="right">12.26</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.86</td>
    <td align="right">8.64</td>
    <td align="right">8.62</td>
    <td align="right">8.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.72</td>
    <td align="right">23.73</td>
    <td align="right">23.74</td>
    <td align="right">23.74</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.00</td>
    <td align="right">24.54</td>
    <td align="right">24.58</td>
    <td align="right">24.53</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.96</td>
    <td align="right">16.66</td>
    <td align="right">16.66</td>
    <td align="right">16.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.31</td>
    <td align="right">29.98</td>
    <td align="right">30.00</td>
    <td align="right">29.99</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.66</td>
    <td align="right">31.30</td>
    <td align="right">31.33</td>
    <td align="right">31.34</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.16</td>
    <td align="right">18.69</td>
    <td align="right">18.71</td>
    <td align="right">18.70</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.44</td>
    <td align="right">4.97</td>
    <td align="right">5.01</td>
    <td align="right">5.03</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.09</td>
    <td align="right">7.00</td>
    <td align="right">6.98</td>
    <td align="right">6.95</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.15</td>
    <td align="right">6.63</td>
    <td align="right">6.70</td>
    <td align="right">6.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.81</td>
    <td align="right">9.28</td>
    <td align="right">9.29</td>
    <td align="right">9.25</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.90</td>
    <td align="right">9.89</td>
    <td align="right">9.86</td>
    <td align="right">9.91</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.37</td>
    <td align="right">11.88</td>
    <td align="right">11.86</td>
    <td align="right">11.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.39</td>
    <td align="right">16.24</td>
    <td align="right">10.38</td>
    <td align="right">20.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.93</td>
    <td align="right">21.33</td>
    <td align="right">16.25</td>
    <td align="right">27.00</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.99</td>
    <td align="right">21.37</td>
    <td align="right">15.60</td>
    <td align="right">26.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.69</td>
    <td align="right">18.45</td>
    <td align="right">11.67</td>
    <td align="right">22.67</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.18</td>
    <td align="right">29.51</td>
    <td align="right">18.55</td>
    <td align="right">32.61</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.43</td>
    <td align="right">26.77</td>
    <td align="right">17.61</td>
    <td align="right">31.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.55</td>
    <td align="right">4.03</td>
    <td align="right">4.01</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.63</td>
    <td align="right">6.43</td>
    <td align="right">6.45</td>
    <td align="right">6.42</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.38</td>
    <td align="right">5.83</td>
    <td align="right">5.81</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.78</td>
    <td align="right">9.22</td>
    <td align="right">9.25</td>
    <td align="right">9.22</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.97</td>
    <td align="right">9.96</td>
    <td align="right">9.94</td>
    <td align="right">9.91</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.61</td>
    <td align="right">12.18</td>
    <td align="right">12.18</td>
    <td align="right">12.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.56</td>
    <td align="right">16.54</td>
    <td align="right">16.56</td>
    <td align="right">16.54</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.02</td>
    <td align="right">21.87</td>
    <td align="right">21.88</td>
    <td align="right">21.88</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.77</td>
    <td align="right">21.65</td>
    <td align="right">21.66</td>
    <td align="right">21.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.71</td>
    <td align="right">18.62</td>
    <td align="right">18.59</td>
    <td align="right">18.60</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.22</td>
    <td align="right">30.92</td>
    <td align="right">30.90</td>
    <td align="right">30.91</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.61</td>
    <td align="right">30.98</td>
    <td align="right">31.00</td>
    <td align="right">31.05</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.56</td>
    <td align="right">4.26</td>
    <td align="right">4.24</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.80</td>
    <td align="right">6.80</td>
    <td align="right">6.81</td>
    <td align="right">6.79</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.83</td>
    <td align="right">5.27</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.36</td>
    <td align="right">9.42</td>
    <td align="right">9.43</td>
    <td align="right">9.48</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.50</td>
    <td align="right">10.04</td>
    <td align="right">10.06</td>
    <td align="right">10.09</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.03</td>
    <td align="right">11.57</td>
    <td align="right">11.58</td>
    <td align="right">11.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.24</td>
    <td align="right">16.24</td>
    <td align="right">10.22</td>
    <td align="right">20.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.29</td>
    <td align="right">20.35</td>
    <td align="right">14.36</td>
    <td align="right">26.07</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.87</td>
    <td align="right">19.27</td>
    <td align="right">14.48</td>
    <td align="right">26.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.51</td>
    <td align="right">18.37</td>
    <td align="right">11.27</td>
    <td align="right">22.78</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.21</td>
    <td align="right">27.13</td>
    <td align="right">16.21</td>
    <td align="right">30.99</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.08</td>
    <td align="right">27.31</td>
    <td align="right">16.37</td>
    <td align="right">30.39</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.08</td>
    <td align="right">4.97</td>
    <td align="right">5.00</td>
    <td align="right">4.98</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.34</td>
    <td align="right">5.01</td>
    <td align="right">5.03</td>
    <td align="right">5.01</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.73</td>
    <td align="right">5.00</td>
    <td align="right">4.99</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.15</td>
    <td align="right">9.15</td>
    <td align="right">9.18</td>
    <td align="right">9.16</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.68</td>
    <td align="right">10.27</td>
    <td align="right">10.28</td>
    <td align="right">10.27</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.07</td>
    <td align="right">11.59</td>
    <td align="right">11.62</td>
    <td align="right">11.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.21</td>
    <td align="right">16.44</td>
    <td align="right">16.46</td>
    <td align="right">16.45</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.12</td>
    <td align="right">21.00</td>
    <td align="right">21.01</td>
    <td align="right">21.00</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.04</td>
    <td align="right">21.67</td>
    <td align="right">21.66</td>
    <td align="right">21.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.44</td>
    <td align="right">18.46</td>
    <td align="right">18.48</td>
    <td align="right">18.48</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.26</td>
    <td align="right">30.35</td>
    <td align="right">30.41</td>
    <td align="right">30.39</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.12</td>
    <td align="right">30.30</td>
    <td align="right">30.34</td>
    <td align="right">30.35</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.99</td>
    <td align="right">9.15</td>
    <td align="right">15.44</td>
    <td align="right">15.40</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.96</td>
    <td align="right">10.09</td>
    <td align="right">19.53</td>
    <td align="right">17.30</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.71</td>
    <td align="right">13.98</td>
    <td align="right">20.85</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.40</td>
    <td align="right">17.93</td>
    <td align="right">17.77</td>
    <td align="right">22.60</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">24.66</td>
    <td align="right">22.44</td>
    <td align="right">19.22</td>
    <td align="right">25.23</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.40</td>
    <td align="right">28.09</td>
    <td align="right">26.38</td>
    <td align="right">29.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.56</td>
    <td align="right">27.12</td>
    <td align="right">21.66</td>
    <td align="right">29.78</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.25</td>
    <td align="right">33.12</td>
    <td align="right">24.63</td>
    <td align="right">36.26</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.06</td>
    <td align="right">43.74</td>
    <td align="right">29.99</td>
    <td align="right">40.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.25</td>
    <td align="right">40.97</td>
    <td align="right">24.56</td>
    <td align="right">42.40</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.54</td>
    <td align="right">40.40</td>
    <td align="right">26.46</td>
    <td align="right">43.56</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.30</td>
    <td align="right">70.24</td>
    <td align="right">40.75</td>
    <td align="right">57.28</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.14</td>
    <td align="right">9.33</td>
    <td align="right">9.32</td>
    <td align="right">9.34</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.45</td>
    <td align="right">10.69</td>
    <td align="right">10.72</td>
    <td align="right">10.70</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.56</td>
    <td align="right">14.37</td>
    <td align="right">14.39</td>
    <td align="right">14.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.64</td>
    <td align="right">17.70</td>
    <td align="right">17.71</td>
    <td align="right">17.78</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.06</td>
    <td align="right">21.42</td>
    <td align="right">21.45</td>
    <td align="right">21.45</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.79</td>
    <td align="right">32.96</td>
    <td align="right">33.03</td>
    <td align="right">33.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.04</td>
    <td align="right">32.23</td>
    <td align="right">32.16</td>
    <td align="right">32.17</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.45</td>
    <td align="right">40.00</td>
    <td align="right">39.99</td>
    <td align="right">39.89</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.25</td>
    <td align="right">50.76</td>
    <td align="right">50.75</td>
    <td align="right">50.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.12</td>
    <td align="right">42.82</td>
    <td align="right">42.79</td>
    <td align="right">42.74</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.62</td>
    <td align="right">51.20</td>
    <td align="right">51.20</td>
    <td align="right">51.31</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.87</td>
    <td align="right">75.05</td>
    <td align="right">75.14</td>
    <td align="right">74.95</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.56</td>
    <td align="right">9.21</td>
    <td align="right">15.36</td>
    <td align="right">15.31</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.31</td>
    <td align="right">9.38</td>
    <td align="right">18.96</td>
    <td align="right">17.02</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.54</td>
    <td align="right">13.91</td>
    <td align="right">19.85</td>
    <td align="right">17.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.09</td>
    <td align="right">18.64</td>
    <td align="right">18.15</td>
    <td align="right">22.78</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.93</td>
    <td align="right">21.16</td>
    <td align="right">18.64</td>
    <td align="right">24.55</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">32.32</td>
    <td align="right">29.91</td>
    <td align="right">24.29</td>
    <td align="right">28.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.50</td>
    <td align="right">27.14</td>
    <td align="right">21.28</td>
    <td align="right">30.39</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.05</td>
    <td align="right">33.16</td>
    <td align="right">24.40</td>
    <td align="right">36.24</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.91</td>
    <td align="right">44.97</td>
    <td align="right">23.18</td>
    <td align="right">39.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.53</td>
    <td align="right">41.32</td>
    <td align="right">24.69</td>
    <td align="right">42.31</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.28</td>
    <td align="right">39.60</td>
    <td align="right">26.41</td>
    <td align="right">42.63</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.63</td>
    <td align="right">71.64</td>
    <td align="right">30.67</td>
    <td align="right">57.92</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.84</td>
    <td align="right">9.59</td>
    <td align="right">9.61</td>
    <td align="right">9.57</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.36</td>
    <td align="right">10.60</td>
    <td align="right">10.59</td>
    <td align="right">10.60</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">17.76</td>
    <td align="right">17.91</td>
    <td align="right">17.81</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.06</td>
    <td align="right">17.91</td>
    <td align="right">17.94</td>
    <td align="right">18.01</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.85</td>
    <td align="right">21.08</td>
    <td align="right">21.09</td>
    <td align="right">21.03</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">32.38</td>
    <td align="right">32.89</td>
    <td align="right">32.86</td>
    <td align="right">32.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.14</td>
    <td align="right">32.11</td>
    <td align="right">32.09</td>
    <td align="right">32.02</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.05</td>
    <td align="right">40.14</td>
    <td align="right">40.05</td>
    <td align="right">40.07</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.28</td>
    <td align="right">52.27</td>
    <td align="right">51.98</td>
    <td align="right">52.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.43</td>
    <td align="right">43.05</td>
    <td align="right">43.08</td>
    <td align="right">43.04</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.53</td>
    <td align="right">51.16</td>
    <td align="right">50.93</td>
    <td align="right">50.98</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.39</td>
    <td align="right">76.86</td>
    <td align="right">76.65</td>
    <td align="right">76.92</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.48</td>
    <td align="right">2.64</td>
    <td align="right">1.91</td>
    <td align="right">9.24</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.33</td>
    <td align="right">4.30</td>
    <td align="right">11.29</td>
    <td align="right">8.88</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.49</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.42</td>
    <td align="right">6.20</td>
    <td align="right">11.68</td>
    <td align="right">10.24</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.41</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">1.67</td>
    <td align="right">1.67</td>
    <td align="right">1.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.57</td>
    <td align="right">7.41</td>
    <td align="right">10.82</td>
    <td align="right">11.10</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.92</td>
    <td align="right">9.48</td>
    <td align="right">11.02</td>
    <td align="right">12.84</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
    <td align="right">1.61</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.35</td>
    <td align="right">3.96</td>
    <td align="right">3.95</td>
    <td align="right">3.94</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.29</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.48</td>
    <td align="right">1.48</td>
    <td align="right">1.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.44</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
    <td align="right">5.86</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.41</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">1.67</td>
    <td align="right">1.66</td>
    <td align="right">1.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.56</td>
    <td align="right">7.08</td>
    <td align="right">7.10</td>
    <td align="right">7.12</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.62</td>
    <td align="right">1.91</td>
    <td align="right">1.92</td>
    <td align="right">1.91</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.89</td>
    <td align="right">9.12</td>
    <td align="right">9.13</td>
    <td align="right">9.12</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">2.10</td>
    <td align="right">2.10</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.61</td>
    <td align="right">1.61</td>
    <td align="right">1.60</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">5.52</td>
    <td align="right">3.81</td>
    <td align="right">11.60</td>
    <td align="right">8.42</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.18</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.29</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.33</td>
    <td align="right">5.45</td>
    <td align="right">12.04</td>
    <td align="right">9.94</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.33</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.45</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.51</td>
    <td align="right">6.64</td>
    <td align="right">11.42</td>
    <td align="right">10.75</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.54</td>
    <td align="right">1.82</td>
    <td align="right">1.83</td>
    <td align="right">1.82</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.65</td>
    <td align="right">1.84</td>
    <td align="right">1.86</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.53</td>
    <td align="right">8.56</td>
    <td align="right">11.68</td>
    <td align="right">11.89</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">2.04</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.63</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
    <td align="right">1.61</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">5.54</td>
    <td align="right">3.57</td>
    <td align="right">3.56</td>
    <td align="right">3.55</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.17</td>
    <td align="right">1.42</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.31</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.43</td>
    <td align="right">5.42</td>
    <td align="right">5.42</td>
    <td align="right">5.42</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.35</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.65</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.47</td>
    <td align="right">1.65</td>
    <td align="right">1.65</td>
    <td align="right">1.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.54</td>
    <td align="right">6.58</td>
    <td align="right">6.55</td>
    <td align="right">6.55</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.53</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.62</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.47</td>
    <td align="right">8.46</td>
    <td align="right">8.48</td>
    <td align="right">8.50</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.62</td>
    <td align="right">1.61</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.26</td>
    <td align="right">2.75</td>
    <td align="right">9.28</td>
    <td align="right">7.42</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.27</td>
    <td align="right">2.77</td>
    <td align="right">8.73</td>
    <td align="right">7.19</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.03</td>
    <td align="right">1.72</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">4.12</td>
    <td align="right">10.64</td>
    <td align="right">8.91</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.82</td>
    <td align="right">3.76</td>
    <td align="right">9.47</td>
    <td align="right">8.01</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.51</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">5.11</td>
    <td align="right">10.61</td>
    <td align="right">9.45</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">4.99</td>
    <td align="right">9.86</td>
    <td align="right">9.20</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.90</td>
    <td align="right">2.41</td>
    <td align="right">1.75</td>
    <td align="right">11.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.66</td>
    <td align="right">5.89</td>
    <td align="right">10.27</td>
    <td align="right">9.76</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.80</td>
    <td align="right">6.07</td>
    <td align="right">10.14</td>
    <td align="right">9.82</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.90</td>
    <td align="right">2.93</td>
    <td align="right">1.70</td>
    <td align="right">11.51</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">1.82</td>
    <td align="right">1.83</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.26</td>
    <td align="right">1.90</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.02</td>
    <td align="right">1.72</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.80</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.51</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.04</td>
    <td align="right">2.97</td>
    <td align="right">2.98</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.09</td>
    <td align="right">3.10</td>
    <td align="right">3.07</td>
    <td align="right">3.08</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.91</td>
    <td align="right">2.40</td>
    <td align="right">2.39</td>
    <td align="right">2.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.58</td>
    <td align="right">3.40</td>
    <td align="right">3.40</td>
    <td align="right">3.40</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.71</td>
    <td align="right">3.63</td>
    <td align="right">3.62</td>
    <td align="right">3.63</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.92</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">2.92</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.91</td>
    <td align="right">2.68</td>
    <td align="right">9.37</td>
    <td align="right">7.31</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">2.75</td>
    <td align="right">8.96</td>
    <td align="right">7.10</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.63</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">4.05</td>
    <td align="right">10.63</td>
    <td align="right">8.81</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.62</td>
    <td align="right">3.74</td>
    <td align="right">9.81</td>
    <td align="right">7.94</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.41</td>
    <td align="right">1.52</td>
    <td align="right">1.51</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.63</td>
    <td align="right">4.94</td>
    <td align="right">10.62</td>
    <td align="right">9.32</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">4.91</td>
    <td align="right">10.05</td>
    <td align="right">8.98</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.65</td>
    <td align="right">2.49</td>
    <td align="right">1.57</td>
    <td align="right">11.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.11</td>
    <td align="right">5.64</td>
    <td align="right">10.20</td>
    <td align="right">9.64</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.29</td>
    <td align="right">5.97</td>
    <td align="right">10.39</td>
    <td align="right">9.68</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.77</td>
    <td align="right">2.97</td>
    <td align="right">1.55</td>
    <td align="right">11.36</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.90</td>
    <td align="right">1.75</td>
    <td align="right">1.72</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">1.78</td>
    <td align="right">1.78</td>
    <td align="right">1.78</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.62</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.08</td>
    <td align="right">1.89</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.51</td>
    <td align="right">2.22</td>
    <td align="right">2.22</td>
    <td align="right">2.26</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.40</td>
    <td align="right">1.52</td>
    <td align="right">1.51</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.64</td>
    <td align="right">2.76</td>
    <td align="right">2.68</td>
    <td align="right">2.67</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">2.85</td>
    <td align="right">2.87</td>
    <td align="right">2.88</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.69</td>
    <td align="right">2.43</td>
    <td align="right">2.43</td>
    <td align="right">2.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.17</td>
    <td align="right">3.13</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.43</td>
    <td align="right">3.34</td>
    <td align="right">3.38</td>
    <td align="right">3.36</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.77</td>
    <td align="right">2.94</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">2.77</td>
    <td align="right">9.29</td>
    <td align="right">7.41</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.27</td>
    <td align="right">2.77</td>
    <td align="right">8.73</td>
    <td align="right">7.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.04</td>
    <td align="right">1.61</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">4.12</td>
    <td align="right">10.64</td>
    <td align="right">8.88</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">3.76</td>
    <td align="right">9.49</td>
    <td align="right">8.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.88</td>
    <td align="right">2.39</td>
    <td align="right">1.74</td>
    <td align="right">11.51</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.03</td>
    <td align="right">5.09</td>
    <td align="right">10.58</td>
    <td align="right">9.41</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.03</td>
    <td align="right">4.99</td>
    <td align="right">9.88</td>
    <td align="right">9.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.87</td>
    <td align="right">2.87</td>
    <td align="right">1.70</td>
    <td align="right">11.50</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.65</td>
    <td align="right">5.79</td>
    <td align="right">10.18</td>
    <td align="right">9.68</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.72</td>
    <td align="right">6.10</td>
    <td align="right">10.17</td>
    <td align="right">9.86</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.01</td>
    <td align="right">1.71</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.29</td>
    <td align="right">1.87</td>
    <td align="right">1.84</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.31</td>
    <td align="right">1.90</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.06</td>
    <td align="right">1.63</td>
    <td align="right">1.61</td>
    <td align="right">1.61</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.88</td>
    <td align="right">1.88</td>
    <td align="right">1.88</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.81</td>
    <td align="right">2.18</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.86</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.05</td>
    <td align="right">2.97</td>
    <td align="right">2.97</td>
    <td align="right">2.98</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.04</td>
    <td align="right">3.09</td>
    <td align="right">3.09</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.93</td>
    <td align="right">2.84</td>
    <td align="right">2.84</td>
    <td align="right">2.85</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.69</td>
    <td align="right">3.40</td>
    <td align="right">3.42</td>
    <td align="right">3.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.75</td>
    <td align="right">3.59</td>
    <td align="right">3.60</td>
    <td align="right">3.59</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.64</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.91</td>
    <td align="right">2.69</td>
    <td align="right">9.38</td>
    <td align="right">7.33</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">2.76</td>
    <td align="right">8.98</td>
    <td align="right">7.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.68</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.08</td>
    <td align="right">4.04</td>
    <td align="right">10.59</td>
    <td align="right">8.71</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.57</td>
    <td align="right">3.71</td>
    <td align="right">9.76</td>
    <td align="right">7.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.67</td>
    <td align="right">2.50</td>
    <td align="right">1.57</td>
    <td align="right">11.36</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.51</td>
    <td align="right">4.94</td>
    <td align="right">10.64</td>
    <td align="right">9.31</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.51</td>
    <td align="right">4.94</td>
    <td align="right">10.10</td>
    <td align="right">9.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.69</td>
    <td align="right">2.91</td>
    <td align="right">1.53</td>
    <td align="right">11.33</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.17</td>
    <td align="right">5.67</td>
    <td align="right">10.24</td>
    <td align="right">9.68</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.45</td>
    <td align="right">5.98</td>
    <td align="right">10.42</td>
    <td align="right">9.68</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.63</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.96</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.97</td>
    <td align="right">1.81</td>
    <td align="right">1.79</td>
    <td align="right">1.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.70</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.62</td>
    <td align="right">2.24</td>
    <td align="right">2.23</td>
    <td align="right">2.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.75</td>
    <td align="right">2.45</td>
    <td align="right">2.45</td>
    <td align="right">2.45</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.53</td>
    <td align="right">2.69</td>
    <td align="right">2.70</td>
    <td align="right">2.70</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.65</td>
    <td align="right">2.89</td>
    <td align="right">2.83</td>
    <td align="right">2.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.79</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.25</td>
    <td align="right">3.21</td>
    <td align="right">3.12</td>
    <td align="right">3.11</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.37</td>
    <td align="right">3.36</td>
    <td align="right">3.37</td>
    <td align="right">3.38</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.22</td>
    <td align="right">3.45</td>
    <td align="right">10.20</td>
    <td align="right">8.46</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">7.04</td>
    <td align="right">3.90</td>
    <td align="right">12.69</td>
    <td align="right">9.31</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.73</td>
    <td align="right">5.39</td>
    <td align="right">13.04</td>
    <td align="right">10.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.38</td>
    <td align="right">4.59</td>
    <td align="right">9.91</td>
    <td align="right">9.44</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.42</td>
    <td align="right">4.70</td>
    <td align="right">10.35</td>
    <td align="right">10.36</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.92</td>
    <td align="right">7.33</td>
    <td align="right">13.56</td>
    <td align="right">11.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.53</td>
    <td align="right">5.43</td>
    <td align="right">9.69</td>
    <td align="right">9.84</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.54</td>
    <td align="right">5.91</td>
    <td align="right">11.19</td>
    <td align="right">11.20</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.06</td>
    <td align="right">8.00</td>
    <td align="right">12.45</td>
    <td align="right">12.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">6.58</td>
    <td align="right">10.25</td>
    <td align="right">10.69</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.39</td>
    <td align="right">6.39</td>
    <td align="right">10.74</td>
    <td align="right">12.01</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.09</td>
    <td align="right">10.83</td>
    <td align="right">14.46</td>
    <td align="right">13.98</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.21</td>
    <td align="right">3.03</td>
    <td align="right">3.02</td>
    <td align="right">3.03</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.99</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.68</td>
    <td align="right">4.90</td>
    <td align="right">4.90</td>
    <td align="right">4.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.99</td>
    <td align="right">3.99</td>
    <td align="right">3.99</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.38</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.86</td>
    <td align="right">6.86</td>
    <td align="right">6.86</td>
    <td align="right">6.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.47</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.48</td>
    <td align="right">5.34</td>
    <td align="right">5.35</td>
    <td align="right">5.36</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.04</td>
    <td align="right">7.58</td>
    <td align="right">7.58</td>
    <td align="right">7.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.06</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.50</td>
    <td align="right">6.09</td>
    <td align="right">6.08</td>
    <td align="right">6.06</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.17</td>
    <td align="right">10.68</td>
    <td align="right">10.68</td>
    <td align="right">10.69</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.19</td>
    <td align="right">3.43</td>
    <td align="right">10.15</td>
    <td align="right">8.34</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.84</td>
    <td align="right">3.78</td>
    <td align="right">12.63</td>
    <td align="right">9.34</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.64</td>
    <td align="right">5.23</td>
    <td align="right">13.35</td>
    <td align="right">9.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.38</td>
    <td align="right">4.61</td>
    <td align="right">9.79</td>
    <td align="right">9.63</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.29</td>
    <td align="right">4.66</td>
    <td align="right">10.28</td>
    <td align="right">10.20</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.68</td>
    <td align="right">7.10</td>
    <td align="right">13.56</td>
    <td align="right">11.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.44</td>
    <td align="right">5.43</td>
    <td align="right">9.71</td>
    <td align="right">10.19</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.40</td>
    <td align="right">5.87</td>
    <td align="right">11.13</td>
    <td align="right">11.05</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.67</td>
    <td align="right">7.75</td>
    <td align="right">12.02</td>
    <td align="right">11.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">6.57</td>
    <td align="right">10.25</td>
    <td align="right">10.90</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.45</td>
    <td align="right">6.39</td>
    <td align="right">10.74</td>
    <td align="right">11.54</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">14.97</td>
    <td align="right">11.05</td>
    <td align="right">13.31</td>
    <td align="right">13.40</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.17</td>
    <td align="right">3.01</td>
    <td align="right">3.01</td>
    <td align="right">3.02</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.80</td>
    <td align="right">3.74</td>
    <td align="right">3.75</td>
    <td align="right">3.74</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.60</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.66</td>
    <td align="right">4.30</td>
    <td align="right">4.34</td>
    <td align="right">4.31</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.66</td>
    <td align="right">6.80</td>
    <td align="right">6.81</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.47</td>
    <td align="right">4.76</td>
    <td align="right">4.74</td>
    <td align="right">4.76</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.52</td>
    <td align="right">5.45</td>
    <td align="right">5.48</td>
    <td align="right">5.45</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.71</td>
    <td align="right">7.58</td>
    <td align="right">7.56</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.02</td>
    <td align="right">5.98</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.40</td>
    <td align="right">6.16</td>
    <td align="right">6.16</td>
    <td align="right">6.15</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.01</td>
    <td align="right">11.10</td>
    <td align="right">11.12</td>
    <td align="right">11.08</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.57</td>
    <td align="right">11.51</td>
    <td align="right">5.52</td>
    <td align="right">15.32</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.74</td>
    <td align="right">6.26</td>
    <td align="right">12.76</td>
    <td align="right">10.46</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.02</td>
    <td align="right">2.27</td>
    <td align="right">2.30</td>
    <td align="right">2.29</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.11</td>
    <td align="right">2.23</td>
    <td align="right">2.23</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.25</td>
    <td align="right">11.57</td>
    <td align="right">15.77</td>
    <td align="right">14.84</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">4.15</td>
    <td align="right">3.67</td>
    <td align="right">3.88</td>
    <td align="right">3.70</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.20</td>
    <td align="right">3.53</td>
    <td align="right">3.87</td>
    <td align="right">3.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">26.85</td>
    <td align="right">25.12</td>
    <td align="right">17.99</td>
    <td align="right">22.65</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.83</td>
    <td align="right">6.75</td>
    <td align="right">7.23</td>
    <td align="right">7.25</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.85</td>
    <td align="right">6.91</td>
    <td align="right">6.56</td>
    <td align="right">7.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.56</td>
    <td align="right">38.79</td>
    <td align="right">20.55</td>
    <td align="right">31.57</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.08</td>
    <td align="right">8.93</td>
    <td align="right">9.30</td>
    <td align="right">8.64</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.80</td>
    <td align="right">6.91</td>
    <td align="right">7.11</td>
    <td align="right">6.98</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.70</td>
    <td align="right">6.43</td>
    <td align="right">6.47</td>
    <td align="right">6.46</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.98</td>
    <td align="right">2.28</td>
    <td align="right">2.29</td>
    <td align="right">2.26</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.13</td>
    <td align="right">2.18</td>
    <td align="right">2.19</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.62</td>
    <td align="right">12.96</td>
    <td align="right">12.66</td>
    <td align="right">12.26</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.54</td>
    <td align="right">4.05</td>
    <td align="right">3.95</td>
    <td align="right">4.00</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.16</td>
    <td align="right">3.70</td>
    <td align="right">3.60</td>
    <td align="right">3.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.13</td>
    <td align="right">28.03</td>
    <td align="right">28.04</td>
    <td align="right">28.64</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.15</td>
    <td align="right">7.13</td>
    <td align="right">7.21</td>
    <td align="right">7.23</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.92</td>
    <td align="right">6.94</td>
    <td align="right">7.03</td>
    <td align="right">6.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">55.98</td>
    <td align="right">44.86</td>
    <td align="right">42.73</td>
    <td align="right">42.67</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.29</td>
    <td align="right">8.16</td>
    <td align="right">8.42</td>
    <td align="right">8.17</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.93</td>
    <td align="right">6.39</td>
    <td align="right">6.60</td>
    <td align="right">6.39</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">6.57</td>
    <td align="right">5.47</td>
    <td align="right">13.13</td>
    <td align="right">9.91</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.84</td>
    <td align="right">2.14</td>
    <td align="right">2.14</td>
    <td align="right">2.15</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.83</td>
    <td align="right">2.07</td>
    <td align="right">2.08</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.89</td>
    <td align="right">9.84</td>
    <td align="right">16.17</td>
    <td align="right">14.04</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.99</td>
    <td align="right">3.44</td>
    <td align="right">3.46</td>
    <td align="right">3.51</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.03</td>
    <td align="right">3.42</td>
    <td align="right">3.41</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">23.98</td>
    <td align="right">20.57</td>
    <td align="right">18.31</td>
    <td align="right">19.49</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.90</td>
    <td align="right">6.30</td>
    <td align="right">6.27</td>
    <td align="right">6.24</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.86</td>
    <td align="right">6.23</td>
    <td align="right">6.21</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.30</td>
    <td align="right">33.01</td>
    <td align="right">21.08</td>
    <td align="right">27.33</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.13</td>
    <td align="right">8.06</td>
    <td align="right">8.36</td>
    <td align="right">8.06</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.90</td>
    <td align="right">6.56</td>
    <td align="right">6.70</td>
    <td align="right">6.63</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">6.57</td>
    <td align="right">5.68</td>
    <td align="right">5.69</td>
    <td align="right">5.69</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.84</td>
    <td align="right">2.14</td>
    <td align="right">2.15</td>
    <td align="right">2.14</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.83</td>
    <td align="right">2.07</td>
    <td align="right">2.08</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.89</td>
    <td align="right">10.76</td>
    <td align="right">10.76</td>
    <td align="right">10.75</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.99</td>
    <td align="right">3.47</td>
    <td align="right">3.46</td>
    <td align="right">3.44</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.03</td>
    <td align="right">3.41</td>
    <td align="right">3.43</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">23.91</td>
    <td align="right">22.89</td>
    <td align="right">22.85</td>
    <td align="right">22.80</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.95</td>
    <td align="right">6.26</td>
    <td align="right">6.31</td>
    <td align="right">6.25</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.87</td>
    <td align="right">6.21</td>
    <td align="right">6.25</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.23</td>
    <td align="right">38.61</td>
    <td align="right">38.59</td>
    <td align="right">38.59</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.11</td>
    <td align="right">8.09</td>
    <td align="right">8.35</td>
    <td align="right">8.07</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.91</td>
    <td align="right">6.57</td>
    <td align="right">6.69</td>
    <td align="right">6.56</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.67</td>
    <td align="right">3.56</td>
    <td align="right">9.95</td>
    <td align="right">8.38</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.68</td>
    <td align="right">3.60</td>
    <td align="right">9.44</td>
    <td align="right">8.21</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.36</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.63</td>
    <td align="right">6.77</td>
    <td align="right">12.94</td>
    <td align="right">12.12</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.07</td>
    <td align="right">6.72</td>
    <td align="right">11.47</td>
    <td align="right">11.13</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.58</td>
    <td align="right">3.39</td>
    <td align="right">3.41</td>
    <td align="right">3.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.60</td>
    <td align="right">12.85</td>
    <td align="right">14.67</td>
    <td align="right">15.82</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.54</td>
    <td align="right">12.62</td>
    <td align="right">13.86</td>
    <td align="right">15.65</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.39</td>
    <td align="right">7.58</td>
    <td align="right">4.98</td>
    <td align="right">14.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.13</td>
    <td align="right">17.05</td>
    <td align="right">15.25</td>
    <td align="right">19.29</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.64</td>
    <td align="right">18.09</td>
    <td align="right">15.72</td>
    <td align="right">20.23</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.34</td>
    <td align="right">10.09</td>
    <td align="right">5.96</td>
    <td align="right">16.04</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.67</td>
    <td align="right">2.65</td>
    <td align="right">2.66</td>
    <td align="right">2.66</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
    <td align="right">2.68</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.37</td>
    <td align="right">2.54</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.63</td>
    <td align="right">4.02</td>
    <td align="right">3.99</td>
    <td align="right">4.02</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.08</td>
    <td align="right">4.71</td>
    <td align="right">4.60</td>
    <td align="right">4.54</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.58</td>
    <td align="right">3.39</td>
    <td align="right">3.41</td>
    <td align="right">3.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.59</td>
    <td align="right">9.07</td>
    <td align="right">9.08</td>
    <td align="right">9.08</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.58</td>
    <td align="right">9.21</td>
    <td align="right">9.19</td>
    <td align="right">9.20</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.44</td>
    <td align="right">7.58</td>
    <td align="right">7.56</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.14</td>
    <td align="right">12.06</td>
    <td align="right">12.38</td>
    <td align="right">12.04</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.64</td>
    <td align="right">12.73</td>
    <td align="right">12.89</td>
    <td align="right">12.71</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.22</td>
    <td align="right">10.21</td>
    <td align="right">10.68</td>
    <td align="right">10.29</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.27</td>
    <td align="right">3.51</td>
    <td align="right">10.13</td>
    <td align="right">8.34</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.34</td>
    <td align="right">3.60</td>
    <td align="right">9.74</td>
    <td align="right">8.15</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.96</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.54</td>
    <td align="right">6.72</td>
    <td align="right">12.92</td>
    <td align="right">11.93</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.17</td>
    <td align="right">6.80</td>
    <td align="right">11.85</td>
    <td align="right">11.02</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.52</td>
    <td align="right">3.38</td>
    <td align="right">3.39</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.71</td>
    <td align="right">12.73</td>
    <td align="right">15.07</td>
    <td align="right">15.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.81</td>
    <td align="right">12.93</td>
    <td align="right">14.26</td>
    <td align="right">15.60</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.16</td>
    <td align="right">7.93</td>
    <td align="right">5.10</td>
    <td align="right">14.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.91</td>
    <td align="right">16.90</td>
    <td align="right">15.20</td>
    <td align="right">19.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.61</td>
    <td align="right">18.55</td>
    <td align="right">15.86</td>
    <td align="right">19.98</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.38</td>
    <td align="right">10.67</td>
    <td align="right">6.30</td>
    <td align="right">16.09</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.26</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.35</td>
    <td align="right">2.60</td>
    <td align="right">2.61</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.97</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.58</td>
    <td align="right">3.99</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.17</td>
    <td align="right">4.94</td>
    <td align="right">4.81</td>
    <td align="right">4.76</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.53</td>
    <td align="right">3.38</td>
    <td align="right">3.39</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.70</td>
    <td align="right">9.24</td>
    <td align="right">9.24</td>
    <td align="right">9.20</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.80</td>
    <td align="right">9.27</td>
    <td align="right">9.27</td>
    <td align="right">9.25</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.22</td>
    <td align="right">7.95</td>
    <td align="right">7.92</td>
    <td align="right">7.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.94</td>
    <td align="right">12.33</td>
    <td align="right">12.51</td>
    <td align="right">12.33</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.58</td>
    <td align="right">12.86</td>
    <td align="right">12.91</td>
    <td align="right">12.87</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.53</td>
    <td align="right">10.78</td>
    <td align="right">11.07</td>
    <td align="right">10.79</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.34</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.67</td>
    <td align="right">3.56</td>
    <td align="right">9.96</td>
    <td align="right">8.38</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">3.59</td>
    <td align="right">9.45</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.83</td>
    <td align="right">3.09</td>
    <td align="right">3.20</td>
    <td align="right">3.22</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.64</td>
    <td align="right">6.77</td>
    <td align="right">12.93</td>
    <td align="right">12.17</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.07</td>
    <td align="right">6.73</td>
    <td align="right">11.48</td>
    <td align="right">11.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.41</td>
    <td align="right">7.57</td>
    <td align="right">4.96</td>
    <td align="right">14.23</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.61</td>
    <td align="right">12.84</td>
    <td align="right">14.67</td>
    <td align="right">15.84</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.54</td>
    <td align="right">12.61</td>
    <td align="right">13.89</td>
    <td align="right">15.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.33</td>
    <td align="right">10.08</td>
    <td align="right">5.97</td>
    <td align="right">15.81</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.18</td>
    <td align="right">17.04</td>
    <td align="right">15.27</td>
    <td align="right">19.30</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.67</td>
    <td align="right">18.08</td>
    <td align="right">15.72</td>
    <td align="right">20.24</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.34</td>
    <td align="right">2.54</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">2.66</td>
    <td align="right">2.67</td>
    <td align="right">2.66</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.81</td>
    <td align="right">3.08</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.62</td>
    <td align="right">4.02</td>
    <td align="right">4.00</td>
    <td align="right">3.98</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.06</td>
    <td align="right">4.69</td>
    <td align="right">4.56</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.41</td>
    <td align="right">7.55</td>
    <td align="right">7.57</td>
    <td align="right">7.53</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.61</td>
    <td align="right">9.10</td>
    <td align="right">9.10</td>
    <td align="right">9.08</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.61</td>
    <td align="right">9.22</td>
    <td align="right">9.22</td>
    <td align="right">9.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.45</td>
    <td align="right">10.34</td>
    <td align="right">10.72</td>
    <td align="right">10.33</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.19</td>
    <td align="right">12.05</td>
    <td align="right">12.39</td>
    <td align="right">12.09</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.65</td>
    <td align="right">12.73</td>
    <td align="right">12.91</td>
    <td align="right">12.72</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">1.98</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.26</td>
    <td align="right">3.51</td>
    <td align="right">10.14</td>
    <td align="right">8.32</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.34</td>
    <td align="right">3.61</td>
    <td align="right">9.75</td>
    <td align="right">8.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.65</td>
    <td align="right">3.43</td>
    <td align="right">3.39</td>
    <td align="right">3.39</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.54</td>
    <td align="right">6.74</td>
    <td align="right">12.92</td>
    <td align="right">11.88</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.15</td>
    <td align="right">6.79</td>
    <td align="right">11.83</td>
    <td align="right">11.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.28</td>
    <td align="right">8.00</td>
    <td align="right">5.21</td>
    <td align="right">14.13</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.71</td>
    <td align="right">12.74</td>
    <td align="right">15.02</td>
    <td align="right">15.71</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.81</td>
    <td align="right">12.92</td>
    <td align="right">14.27</td>
    <td align="right">15.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.63</td>
    <td align="right">10.89</td>
    <td align="right">6.37</td>
    <td align="right">15.89</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.92</td>
    <td align="right">16.90</td>
    <td align="right">15.20</td>
    <td align="right">19.10</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.62</td>
    <td align="right">18.52</td>
    <td align="right">15.86</td>
    <td align="right">19.98</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">1.98</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.27</td>
    <td align="right">2.54</td>
    <td align="right">2.55</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.34</td>
    <td align="right">2.59</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.67</td>
    <td align="right">3.41</td>
    <td align="right">3.39</td>
    <td align="right">3.39</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.54</td>
    <td align="right">3.98</td>
    <td align="right">3.96</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.16</td>
    <td align="right">4.93</td>
    <td align="right">4.81</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.24</td>
    <td align="right">8.00</td>
    <td align="right">8.00</td>
    <td align="right">7.98</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.71</td>
    <td align="right">9.21</td>
    <td align="right">9.25</td>
    <td align="right">9.23</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.86</td>
    <td align="right">9.27</td>
    <td align="right">9.29</td>
    <td align="right">9.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.63</td>
    <td align="right">11.01</td>
    <td align="right">11.23</td>
    <td align="right">11.01</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.94</td>
    <td align="right">12.36</td>
    <td align="right">12.51</td>
    <td align="right">12.34</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.59</td>
    <td align="right">12.86</td>
    <td align="right">12.91</td>
    <td align="right">12.90</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.47</td>
    <td align="right">4.43</td>
    <td align="right">11.06</td>
    <td align="right">9.70</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.63</td>
    <td align="right">4.88</td>
    <td align="right">13.34</td>
    <td align="right">10.37</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.89</td>
    <td align="right">6.79</td>
    <td align="right">14.42</td>
    <td align="right">11.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">7.99</td>
    <td align="right">7.42</td>
    <td align="right">11.92</td>
    <td align="right">12.78</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.16</td>
    <td align="right">7.81</td>
    <td align="right">12.33</td>
    <td align="right">13.58</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.06</td>
    <td align="right">11.59</td>
    <td align="right">17.34</td>
    <td align="right">15.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.12</td>
    <td align="right">12.42</td>
    <td align="right">13.43</td>
    <td align="right">16.39</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.71</td>
    <td align="right">14.32</td>
    <td align="right">15.68</td>
    <td align="right">18.78</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.26</td>
    <td align="right">19.16</td>
    <td align="right">18.13</td>
    <td align="right">20.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.48</td>
    <td align="right">16.38</td>
    <td align="right">15.12</td>
    <td align="right">19.94</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.05</td>
    <td align="right">18.97</td>
    <td align="right">16.59</td>
    <td align="right">22.59</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.63</td>
    <td align="right">34.87</td>
    <td align="right">26.60</td>
    <td align="right">31.85</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.47</td>
    <td align="right">4.29</td>
    <td align="right">4.33</td>
    <td align="right">4.29</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.65</td>
    <td align="right">5.13</td>
    <td align="right">5.15</td>
    <td align="right">5.14</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.88</td>
    <td align="right">6.75</td>
    <td align="right">6.75</td>
    <td align="right">6.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">7.94</td>
    <td align="right">7.72</td>
    <td align="right">7.74</td>
    <td align="right">7.69</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.17</td>
    <td align="right">7.96</td>
    <td align="right">7.95</td>
    <td align="right">7.95</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.07</td>
    <td align="right">11.98</td>
    <td align="right">11.97</td>
    <td align="right">11.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.12</td>
    <td align="right">13.15</td>
    <td align="right">13.26</td>
    <td align="right">13.25</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.76</td>
    <td align="right">15.16</td>
    <td align="right">15.22</td>
    <td align="right">15.25</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.34</td>
    <td align="right">20.37</td>
    <td align="right">20.35</td>
    <td align="right">20.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.54</td>
    <td align="right">17.83</td>
    <td align="right">18.25</td>
    <td align="right">17.80</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.04</td>
    <td align="right">20.59</td>
    <td align="right">21.11</td>
    <td align="right">20.61</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.61</td>
    <td align="right">35.70</td>
    <td align="right">35.72</td>
    <td align="right">35.73</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.55</td>
    <td align="right">4.42</td>
    <td align="right">11.06</td>
    <td align="right">9.60</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.51</td>
    <td align="right">4.75</td>
    <td align="right">13.22</td>
    <td align="right">10.39</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.83</td>
    <td align="right">6.57</td>
    <td align="right">14.64</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.30</td>
    <td align="right">7.38</td>
    <td align="right">11.82</td>
    <td align="right">12.82</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.28</td>
    <td align="right">7.97</td>
    <td align="right">12.11</td>
    <td align="right">13.49</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.75</td>
    <td align="right">11.54</td>
    <td align="right">16.46</td>
    <td align="right">14.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.60</td>
    <td align="right">12.39</td>
    <td align="right">13.41</td>
    <td align="right">16.50</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.04</td>
    <td align="right">14.58</td>
    <td align="right">15.47</td>
    <td align="right">18.77</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.85</td>
    <td align="right">19.33</td>
    <td align="right">15.40</td>
    <td align="right">19.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.66</td>
    <td align="right">16.39</td>
    <td align="right">15.11</td>
    <td align="right">19.96</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.89</td>
    <td align="right">19.53</td>
    <td align="right">16.38</td>
    <td align="right">23.08</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.36</td>
    <td align="right">35.70</td>
    <td align="right">17.58</td>
    <td align="right">31.05</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.55</td>
    <td align="right">4.29</td>
    <td align="right">4.31</td>
    <td align="right">4.29</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.49</td>
    <td align="right">5.01</td>
    <td align="right">5.04</td>
    <td align="right">5.01</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.83</td>
    <td align="right">6.39</td>
    <td align="right">6.40</td>
    <td align="right">6.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.33</td>
    <td align="right">7.70</td>
    <td align="right">7.69</td>
    <td align="right">7.70</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.87</td>
    <td align="right">8.12</td>
    <td align="right">8.11</td>
    <td align="right">8.14</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.74</td>
    <td align="right">12.02</td>
    <td align="right">11.95</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.63</td>
    <td align="right">13.18</td>
    <td align="right">13.27</td>
    <td align="right">13.17</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.04</td>
    <td align="right">15.48</td>
    <td align="right">15.47</td>
    <td align="right">15.44</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.83</td>
    <td align="right">20.62</td>
    <td align="right">20.63</td>
    <td align="right">20.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.75</td>
    <td align="right">17.83</td>
    <td align="right">18.25</td>
    <td align="right">17.79</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.90</td>
    <td align="right">21.22</td>
    <td align="right">21.69</td>
    <td align="right">21.24</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.39</td>
    <td align="right">36.99</td>
    <td align="right">36.96</td>
    <td align="right">36.99</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.90</td>
    <td align="right">5.00</td>
    <td align="right">3.64</td>
    <td align="right">10.33</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.30</td>
    <td align="right">11.57</td>
    <td align="right">14.61</td>
    <td align="right">14.13</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.81</td>
    <td align="right">4.02</td>
    <td align="right">8.55</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.37</td>
    <td align="right">4.13</td>
    <td align="right">4.34</td>
    <td align="right">8.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.09</td>
    <td align="right">16.26</td>
    <td align="right">14.69</td>
    <td align="right">17.15</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.43</td>
    <td align="right">4.23</td>
    <td align="right">4.18</td>
    <td align="right">9.04</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.45</td>
    <td align="right">4.42</td>
    <td align="right">9.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.20</td>
    <td align="right">20.50</td>
    <td align="right">14.24</td>
    <td align="right">20.22</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.06</td>
    <td align="right">4.55</td>
    <td align="right">4.46</td>
    <td align="right">9.44</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.69</td>
    <td align="right">4.90</td>
    <td align="right">4.78</td>
    <td align="right">9.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.91</td>
    <td align="right">25.42</td>
    <td align="right">14.19</td>
    <td align="right">22.33</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.75</td>
    <td align="right">4.95</td>
    <td align="right">4.82</td>
    <td align="right">9.82</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.29</td>
    <td align="right">5.24</td>
    <td align="right">5.18</td>
    <td align="right">10.13</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.29</td>
    <td align="right">12.90</td>
    <td align="right">13.07</td>
    <td align="right">18.46</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.79</td>
    <td align="right">3.99</td>
    <td align="right">8.42</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.37</td>
    <td align="right">4.12</td>
    <td align="right">4.35</td>
    <td align="right">8.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.15</td>
    <td align="right">19.07</td>
    <td align="right">18.42</td>
    <td align="right">23.97</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.44</td>
    <td align="right">4.21</td>
    <td align="right">4.18</td>
    <td align="right">9.03</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.51</td>
    <td align="right">4.49</td>
    <td align="right">9.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.27</td>
    <td align="right">23.04</td>
    <td align="right">22.97</td>
    <td align="right">28.67</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.07</td>
    <td align="right">4.56</td>
    <td align="right">4.47</td>
    <td align="right">9.52</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">4.91</td>
    <td align="right">4.79</td>
    <td align="right">9.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.86</td>
    <td align="right">28.19</td>
    <td align="right">28.06</td>
    <td align="right">33.92</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.73</td>
    <td align="right">4.97</td>
    <td align="right">4.82</td>
    <td align="right">10.00</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.30</td>
    <td align="right">5.28</td>
    <td align="right">5.19</td>
    <td align="right">10.39</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.21</td>
    <td align="right">11.84</td>
    <td align="right">15.60</td>
    <td align="right">14.38</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.88</td>
    <td align="right">3.78</td>
    <td align="right">3.94</td>
    <td align="right">8.41</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.40</td>
    <td align="right">4.12</td>
    <td align="right">4.27</td>
    <td align="right">8.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.00</td>
    <td align="right">17.16</td>
    <td align="right">16.37</td>
    <td align="right">17.97</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.50</td>
    <td align="right">4.18</td>
    <td align="right">4.12</td>
    <td align="right">9.00</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">4.50</td>
    <td align="right">4.42</td>
    <td align="right">9.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.21</td>
    <td align="right">20.98</td>
    <td align="right">15.51</td>
    <td align="right">20.09</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.13</td>
    <td align="right">4.53</td>
    <td align="right">4.40</td>
    <td align="right">9.33</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.64</td>
    <td align="right">4.90</td>
    <td align="right">4.74</td>
    <td align="right">9.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.77</td>
    <td align="right">26.20</td>
    <td align="right">15.88</td>
    <td align="right">23.03</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.80</td>
    <td align="right">4.90</td>
    <td align="right">4.73</td>
    <td align="right">9.92</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.25</td>
    <td align="right">5.26</td>
    <td align="right">5.16</td>
    <td align="right">10.35</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.18</td>
    <td align="right">13.10</td>
    <td align="right">13.15</td>
    <td align="right">18.48</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.87</td>
    <td align="right">3.79</td>
    <td align="right">3.95</td>
    <td align="right">8.42</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.41</td>
    <td align="right">4.12</td>
    <td align="right">4.26</td>
    <td align="right">8.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.01</td>
    <td align="right">19.32</td>
    <td align="right">18.89</td>
    <td align="right">24.54</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.50</td>
    <td align="right">4.19</td>
    <td align="right">4.12</td>
    <td align="right">9.05</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.51</td>
    <td align="right">4.42</td>
    <td align="right">9.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.16</td>
    <td align="right">23.53</td>
    <td align="right">22.81</td>
    <td align="right">28.38</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.11</td>
    <td align="right">4.53</td>
    <td align="right">4.40</td>
    <td align="right">9.44</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.65</td>
    <td align="right">4.87</td>
    <td align="right">4.73</td>
    <td align="right">9.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.58</td>
    <td align="right">28.96</td>
    <td align="right">28.88</td>
    <td align="right">34.66</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.76</td>
    <td align="right">4.88</td>
    <td align="right">4.73</td>
    <td align="right">9.65</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.25</td>
    <td align="right">5.23</td>
    <td align="right">5.14</td>
    <td align="right">10.29</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.44</td>
    <td align="right">7.02</td>
    <td align="right">11.33</td>
    <td align="right">10.59</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.45</td>
    <td align="right">7.56</td>
    <td align="right">12.22</td>
    <td align="right">11.99</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.86</td>
    <td align="right">2.51</td>
    <td align="right">2.84</td>
    <td align="right">8.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">9.84</td>
    <td align="right">11.92</td>
    <td align="right">12.42</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.71</td>
    <td align="right">11.38</td>
    <td align="right">13.22</td>
    <td align="right">14.01</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.82</td>
    <td align="right">3.40</td>
    <td align="right">2.63</td>
    <td align="right">9.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.60</td>
    <td align="right">13.01</td>
    <td align="right">14.13</td>
    <td align="right">15.93</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.22</td>
    <td align="right">14.16</td>
    <td align="right">15.48</td>
    <td align="right">16.43</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">4.90</td>
    <td align="right">3.50</td>
    <td align="right">11.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.67</td>
    <td align="right">14.43</td>
    <td align="right">13.63</td>
    <td align="right">16.43</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.05</td>
    <td align="right">19.91</td>
    <td align="right">16.00</td>
    <td align="right">21.18</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.35</td>
    <td align="right">4.94</td>
    <td align="right">3.52</td>
    <td align="right">11.58</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.41</td>
    <td align="right">4.97</td>
    <td align="right">5.02</td>
    <td align="right">9.46</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.45</td>
    <td align="right">5.42</td>
    <td align="right">5.46</td>
    <td align="right">11.08</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.62</td>
    <td align="right">2.86</td>
    <td align="right">8.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">7.43</td>
    <td align="right">6.94</td>
    <td align="right">12.00</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.69</td>
    <td align="right">7.62</td>
    <td align="right">7.55</td>
    <td align="right">13.24</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.75</td>
    <td align="right">2.56</td>
    <td align="right">2.47</td>
    <td align="right">8.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.54</td>
    <td align="right">9.33</td>
    <td align="right">9.14</td>
    <td align="right">14.00</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.14</td>
    <td align="right">10.77</td>
    <td align="right">10.31</td>
    <td align="right">15.69</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">3.90</td>
    <td align="right">3.75</td>
    <td align="right">10.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.64</td>
    <td align="right">10.41</td>
    <td align="right">10.19</td>
    <td align="right">15.13</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.02</td>
    <td align="right">12.35</td>
    <td align="right">12.20</td>
    <td align="right">17.30</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.33</td>
    <td align="right">3.89</td>
    <td align="right">3.71</td>
    <td align="right">10.46</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.39</td>
    <td align="right">7.03</td>
    <td align="right">11.36</td>
    <td align="right">11.01</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.53</td>
    <td align="right">7.57</td>
    <td align="right">12.26</td>
    <td align="right">11.65</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.82</td>
    <td align="right">2.47</td>
    <td align="right">2.79</td>
    <td align="right">8.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.15</td>
    <td align="right">10.07</td>
    <td align="right">12.06</td>
    <td align="right">12.45</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.55</td>
    <td align="right">11.22</td>
    <td align="right">13.24</td>
    <td align="right">14.38</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">3.38</td>
    <td align="right">2.59</td>
    <td align="right">9.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.54</td>
    <td align="right">13.25</td>
    <td align="right">14.45</td>
    <td align="right">16.04</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.24</td>
    <td align="right">14.23</td>
    <td align="right">15.38</td>
    <td align="right">16.92</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.34</td>
    <td align="right">4.80</td>
    <td align="right">3.31</td>
    <td align="right">11.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.68</td>
    <td align="right">14.97</td>
    <td align="right">13.71</td>
    <td align="right">17.43</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.05</td>
    <td align="right">20.18</td>
    <td align="right">15.87</td>
    <td align="right">21.16</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.37</td>
    <td align="right">4.80</td>
    <td align="right">3.28</td>
    <td align="right">11.36</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.41</td>
    <td align="right">4.96</td>
    <td align="right">5.03</td>
    <td align="right">9.48</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.53</td>
    <td align="right">5.41</td>
    <td align="right">5.52</td>
    <td align="right">10.99</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.83</td>
    <td align="right">2.64</td>
    <td align="right">2.84</td>
    <td align="right">8.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.17</td>
    <td align="right">7.37</td>
    <td align="right">6.93</td>
    <td align="right">12.21</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.50</td>
    <td align="right">7.70</td>
    <td align="right">7.47</td>
    <td align="right">13.16</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.59</td>
    <td align="right">2.44</td>
    <td align="right">8.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.53</td>
    <td align="right">9.35</td>
    <td align="right">9.17</td>
    <td align="right">14.22</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.24</td>
    <td align="right">10.70</td>
    <td align="right">10.09</td>
    <td align="right">15.61</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.34</td>
    <td align="right">3.85</td>
    <td align="right">3.65</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.70</td>
    <td align="right">10.47</td>
    <td align="right">10.34</td>
    <td align="right">15.27</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.16</td>
    <td align="right">12.39</td>
    <td align="right">12.24</td>
    <td align="right">17.39</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.37</td>
    <td align="right">3.87</td>
    <td align="right">3.66</td>
    <td align="right">10.49</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.85</td>
    <td align="right">2.40</td>
    <td align="right">2.67</td>
    <td align="right">8.56</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">3.54</td>
    <td align="right">3.75</td>
    <td align="right">10.46</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.38</td>
    <td align="right">3.63</td>
    <td align="right">10.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">3.83</td>
    <td align="right">3.00</td>
    <td align="right">9.93</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">4.23</td>
    <td align="right">3.51</td>
    <td align="right">10.52</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">4.91</td>
    <td align="right">4.11</td>
    <td align="right">11.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.41</td>
    <td align="right">4.65</td>
    <td align="right">3.10</td>
    <td align="right">10.81</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.91</td>
    <td align="right">6.65</td>
    <td align="right">5.24</td>
    <td align="right">13.32</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.70</td>
    <td align="right">6.48</td>
    <td align="right">5.09</td>
    <td align="right">13.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.44</td>
    <td align="right">4.68</td>
    <td align="right">3.15</td>
    <td align="right">10.98</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.86</td>
    <td align="right">7.62</td>
    <td align="right">5.32</td>
    <td align="right">13.89</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.07</td>
    <td align="right">7.33</td>
    <td align="right">5.15</td>
    <td align="right">13.59</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.82</td>
    <td align="right">2.52</td>
    <td align="right">2.70</td>
    <td align="right">8.52</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.72</td>
    <td align="right">3.54</td>
    <td align="right">3.79</td>
    <td align="right">10.38</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.45</td>
    <td align="right">3.68</td>
    <td align="right">10.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">2.59</td>
    <td align="right">2.46</td>
    <td align="right">8.70</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">4.72</td>
    <td align="right">4.53</td>
    <td align="right">10.92</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">5.45</td>
    <td align="right">5.36</td>
    <td align="right">12.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">3.72</td>
    <td align="right">3.52</td>
    <td align="right">10.15</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.89</td>
    <td align="right">7.16</td>
    <td align="right">6.88</td>
    <td align="right">13.99</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.69</td>
    <td align="right">6.84</td>
    <td align="right">6.66</td>
    <td align="right">13.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.45</td>
    <td align="right">3.74</td>
    <td align="right">3.53</td>
    <td align="right">10.20</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.84</td>
    <td align="right">8.14</td>
    <td align="right">7.78</td>
    <td align="right">15.07</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.06</td>
    <td align="right">7.82</td>
    <td align="right">7.56</td>
    <td align="right">14.74</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.72</td>
    <td align="right">2.34</td>
    <td align="right">2.57</td>
    <td align="right">8.71</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.63</td>
    <td align="right">3.41</td>
    <td align="right">3.73</td>
    <td align="right">10.50</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.75</td>
    <td align="right">3.28</td>
    <td align="right">3.60</td>
    <td align="right">10.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.19</td>
    <td align="right">3.75</td>
    <td align="right">2.93</td>
    <td align="right">9.78</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.23</td>
    <td align="right">4.24</td>
    <td align="right">3.38</td>
    <td align="right">10.52</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">4.85</td>
    <td align="right">4.09</td>
    <td align="right">11.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">4.63</td>
    <td align="right">3.16</td>
    <td align="right">11.03</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.86</td>
    <td align="right">6.51</td>
    <td align="right">4.97</td>
    <td align="right">13.35</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.62</td>
    <td align="right">6.42</td>
    <td align="right">5.00</td>
    <td align="right">13.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.43</td>
    <td align="right">4.67</td>
    <td align="right">3.15</td>
    <td align="right">11.04</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.45</td>
    <td align="right">7.24</td>
    <td align="right">4.96</td>
    <td align="right">13.73</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.04</td>
    <td align="right">7.23</td>
    <td align="right">5.01</td>
    <td align="right">13.30</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.71</td>
    <td align="right">2.51</td>
    <td align="right">2.65</td>
    <td align="right">8.44</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.64</td>
    <td align="right">3.50</td>
    <td align="right">3.74</td>
    <td align="right">10.50</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">3.39</td>
    <td align="right">3.60</td>
    <td align="right">10.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.19</td>
    <td align="right">2.58</td>
    <td align="right">2.41</td>
    <td align="right">8.94</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.23</td>
    <td align="right">4.74</td>
    <td align="right">4.55</td>
    <td align="right">11.03</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">5.35</td>
    <td align="right">5.22</td>
    <td align="right">11.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.38</td>
    <td align="right">3.65</td>
    <td align="right">3.47</td>
    <td align="right">10.56</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.89</td>
    <td align="right">7.07</td>
    <td align="right">6.89</td>
    <td align="right">13.83</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.66</td>
    <td align="right">6.73</td>
    <td align="right">6.48</td>
    <td align="right">13.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.52</td>
    <td align="right">3.63</td>
    <td align="right">3.44</td>
    <td align="right">10.47</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.45</td>
    <td align="right">8.04</td>
    <td align="right">7.75</td>
    <td align="right">14.95</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.02</td>
    <td align="right">7.67</td>
    <td align="right">7.45</td>
    <td align="right">14.67</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.09</td>
    <td align="right">6.97</td>
    <td align="right">11.49</td>
    <td align="right">11.08</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.31</td>
    <td align="right">9.80</td>
    <td align="right">14.18</td>
    <td align="right">13.07</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.09</td>
    <td align="right">12.46</td>
    <td align="right">16.38</td>
    <td align="right">14.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.44</td>
    <td align="right">10.06</td>
    <td align="right">12.45</td>
    <td align="right">13.41</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.85</td>
    <td align="right">11.25</td>
    <td align="right">13.76</td>
    <td align="right">14.93</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.69</td>
    <td align="right">16.17</td>
    <td align="right">17.11</td>
    <td align="right">17.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.48</td>
    <td align="right">11.71</td>
    <td align="right">11.83</td>
    <td align="right">14.44</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.34</td>
    <td align="right">13.50</td>
    <td align="right">14.20</td>
    <td align="right">16.40</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.54</td>
    <td align="right">18.46</td>
    <td align="right">17.76</td>
    <td align="right">19.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.75</td>
    <td align="right">14.25</td>
    <td align="right">12.56</td>
    <td align="right">16.95</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.45</td>
    <td align="right">15.48</td>
    <td align="right">12.56</td>
    <td align="right">17.26</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.55</td>
    <td align="right">24.19</td>
    <td align="right">19.55</td>
    <td align="right">22.91</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.10</td>
    <td align="right">6.39</td>
    <td align="right">6.13</td>
    <td align="right">11.00</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.50</td>
    <td align="right">8.02</td>
    <td align="right">8.09</td>
    <td align="right">13.19</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.12</td>
    <td align="right">9.03</td>
    <td align="right">9.18</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.45</td>
    <td align="right">8.26</td>
    <td align="right">7.99</td>
    <td align="right">13.13</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.83</td>
    <td align="right">9.90</td>
    <td align="right">9.45</td>
    <td align="right">14.96</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.65</td>
    <td align="right">13.05</td>
    <td align="right">12.86</td>
    <td align="right">17.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.48</td>
    <td align="right">10.59</td>
    <td align="right">10.52</td>
    <td align="right">15.01</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.32</td>
    <td align="right">13.44</td>
    <td align="right">13.06</td>
    <td align="right">17.09</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.49</td>
    <td align="right">15.17</td>
    <td align="right">15.15</td>
    <td align="right">20.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.79</td>
    <td align="right">13.15</td>
    <td align="right">13.04</td>
    <td align="right">16.78</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.66</td>
    <td align="right">14.79</td>
    <td align="right">14.73</td>
    <td align="right">18.43</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.55</td>
    <td align="right">23.58</td>
    <td align="right">23.14</td>
    <td align="right">26.69</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.38</td>
    <td align="right">7.12</td>
    <td align="right">11.62</td>
    <td align="right">11.04</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.38</td>
    <td align="right">9.72</td>
    <td align="right">14.15</td>
    <td align="right">12.98</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.18</td>
    <td align="right">12.61</td>
    <td align="right">16.53</td>
    <td align="right">14.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.71</td>
    <td align="right">10.41</td>
    <td align="right">12.41</td>
    <td align="right">13.44</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.84</td>
    <td align="right">11.38</td>
    <td align="right">13.56</td>
    <td align="right">14.89</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.78</td>
    <td align="right">16.55</td>
    <td align="right">17.33</td>
    <td align="right">18.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.84</td>
    <td align="right">11.77</td>
    <td align="right">11.85</td>
    <td align="right">14.80</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.32</td>
    <td align="right">13.34</td>
    <td align="right">14.15</td>
    <td align="right">16.27</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.35</td>
    <td align="right">18.65</td>
    <td align="right">15.13</td>
    <td align="right">19.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.14</td>
    <td align="right">14.93</td>
    <td align="right">12.86</td>
    <td align="right">17.62</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.37</td>
    <td align="right">15.36</td>
    <td align="right">12.56</td>
    <td align="right">17.35</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.66</td>
    <td align="right">24.18</td>
    <td align="right">15.64</td>
    <td align="right">22.57</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.39</td>
    <td align="right">6.59</td>
    <td align="right">6.29</td>
    <td align="right">11.31</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.54</td>
    <td align="right">8.04</td>
    <td align="right">8.05</td>
    <td align="right">13.14</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.14</td>
    <td align="right">9.36</td>
    <td align="right">9.49</td>
    <td align="right">14.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.71</td>
    <td align="right">8.61</td>
    <td align="right">8.16</td>
    <td align="right">13.38</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.84</td>
    <td align="right">9.87</td>
    <td align="right">9.22</td>
    <td align="right">14.88</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.80</td>
    <td align="right">13.57</td>
    <td align="right">13.43</td>
    <td align="right">18.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.89</td>
    <td align="right">11.42</td>
    <td align="right">11.36</td>
    <td align="right">15.97</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.33</td>
    <td align="right">13.47</td>
    <td align="right">13.31</td>
    <td align="right">17.13</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.33</td>
    <td align="right">15.08</td>
    <td align="right">14.95</td>
    <td align="right">20.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.12</td>
    <td align="right">13.47</td>
    <td align="right">13.44</td>
    <td align="right">17.17</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.42</td>
    <td align="right">14.71</td>
    <td align="right">14.63</td>
    <td align="right">18.04</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.66</td>
    <td align="right">22.73</td>
    <td align="right">22.37</td>
    <td align="right">27.34</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">46.02</td>
    <td align="right">22.58</td>
    <td align="right">11.37</td>
    <td align="right">27.43</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.06</td>
    <td align="right">12.11</td>
    <td align="right">15.94</td>
    <td align="right">15.33</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.14</td>
    <td align="right">4.01</td>
    <td align="right">4.27</td>
    <td align="right">9.53</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.70</td>
    <td align="right">4.34</td>
    <td align="right">4.60</td>
    <td align="right">9.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">18.29</td>
    <td align="right">18.14</td>
    <td align="right">16.48</td>
    <td align="right">19.62</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.05</td>
    <td align="right">5.64</td>
    <td align="right">5.75</td>
    <td align="right">11.00</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.98</td>
    <td align="right">6.05</td>
    <td align="right">6.02</td>
    <td align="right">10.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.31</td>
    <td align="right">80.49</td>
    <td align="right">26.74</td>
    <td align="right">56.26</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.54</td>
    <td align="right">14.24</td>
    <td align="right">13.86</td>
    <td align="right">18.28</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.43</td>
    <td align="right">15.61</td>
    <td align="right">15.17</td>
    <td align="right">19.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.89</td>
    <td align="right">121.60</td>
    <td align="right">31.73</td>
    <td align="right">80.34</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.75</td>
    <td align="right">18.90</td>
    <td align="right">18.55</td>
    <td align="right">22.80</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">21.04</td>
    <td align="right">19.38</td>
    <td align="right">19.29</td>
    <td align="right">23.34</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.95</td>
    <td align="right">13.54</td>
    <td align="right">13.65</td>
    <td align="right">19.22</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.10</td>
    <td align="right">4.01</td>
    <td align="right">4.26</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.66</td>
    <td align="right">4.34</td>
    <td align="right">4.62</td>
    <td align="right">9.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">17.80</td>
    <td align="right">63.96</td>
    <td align="right">63.68</td>
    <td align="right">68.40</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.16</td>
    <td align="right">5.54</td>
    <td align="right">5.59</td>
    <td align="right">10.89</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.92</td>
    <td align="right">6.02</td>
    <td align="right">6.09</td>
    <td align="right">10.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.16</td>
    <td align="right">85.88</td>
    <td align="right">85.71</td>
    <td align="right">90.64</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.67</td>
    <td align="right">13.90</td>
    <td align="right">13.53</td>
    <td align="right">17.92</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.42</td>
    <td align="right">15.59</td>
    <td align="right">15.14</td>
    <td align="right">19.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.65</td>
    <td align="right">129.75</td>
    <td align="right">129.42</td>
    <td align="right">133.97</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.77</td>
    <td align="right">18.84</td>
    <td align="right">18.42</td>
    <td align="right">22.80</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.94</td>
    <td align="right">19.46</td>
    <td align="right">19.27</td>
    <td align="right">23.44</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.89</td>
    <td align="right">18.75</td>
    <td align="right">18.99</td>
    <td align="right">19.49</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.19</td>
    <td align="right">3.99</td>
    <td align="right">4.22</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.71</td>
    <td align="right">4.30</td>
    <td align="right">4.53</td>
    <td align="right">9.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">16.80</td>
    <td align="right">19.21</td>
    <td align="right">18.42</td>
    <td align="right">20.27</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.12</td>
    <td align="right">5.85</td>
    <td align="right">5.91</td>
    <td align="right">11.06</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.30</td>
    <td align="right">5.81</td>
    <td align="right">5.81</td>
    <td align="right">10.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.12</td>
    <td align="right">85.11</td>
    <td align="right">29.64</td>
    <td align="right">58.87</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.65</td>
    <td align="right">15.08</td>
    <td align="right">15.11</td>
    <td align="right">19.33</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.42</td>
    <td align="right">17.99</td>
    <td align="right">17.76</td>
    <td align="right">21.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.21</td>
    <td align="right">130.90</td>
    <td align="right">37.11</td>
    <td align="right">85.92</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.82</td>
    <td align="right">18.81</td>
    <td align="right">18.47</td>
    <td align="right">22.81</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.62</td>
    <td align="right">22.28</td>
    <td align="right">22.04</td>
    <td align="right">26.13</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.79</td>
    <td align="right">13.68</td>
    <td align="right">13.67</td>
    <td align="right">19.20</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.19</td>
    <td align="right">4.00</td>
    <td align="right">4.19</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.71</td>
    <td align="right">4.30</td>
    <td align="right">4.54</td>
    <td align="right">9.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">16.81</td>
    <td align="right">20.96</td>
    <td align="right">20.93</td>
    <td align="right">26.60</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.28</td>
    <td align="right">5.88</td>
    <td align="right">5.85</td>
    <td align="right">11.19</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.82</td>
    <td align="right">5.96</td>
    <td align="right">5.96</td>
    <td align="right">10.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.25</td>
    <td align="right">91.85</td>
    <td align="right">91.62</td>
    <td align="right">96.61</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.55</td>
    <td align="right">14.65</td>
    <td align="right">14.51</td>
    <td align="right">18.84</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.72</td>
    <td align="right">16.03</td>
    <td align="right">15.82</td>
    <td align="right">19.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.08</td>
    <td align="right">142.48</td>
    <td align="right">142.29</td>
    <td align="right">146.29</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.87</td>
    <td align="right">18.79</td>
    <td align="right">18.53</td>
    <td align="right">22.57</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.63</td>
    <td align="right">22.26</td>
    <td align="right">22.11</td>
    <td align="right">26.06</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.05</td>
    <td align="right">7.52</td>
    <td align="right">11.98</td>
    <td align="right">11.48</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.63</td>
    <td align="right">8.08</td>
    <td align="right">13.07</td>
    <td align="right">12.82</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.11</td>
    <td align="right">2.63</td>
    <td align="right">3.17</td>
    <td align="right">9.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.31</td>
    <td align="right">12.20</td>
    <td align="right">13.81</td>
    <td align="right">15.19</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.08</td>
    <td align="right">14.29</td>
    <td align="right">14.25</td>
    <td align="right">16.88</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.90</td>
    <td align="right">5.12</td>
    <td align="right">4.49</td>
    <td align="right">10.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.20</td>
    <td align="right">30.37</td>
    <td align="right">22.19</td>
    <td align="right">29.96</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.82</td>
    <td align="right">31.90</td>
    <td align="right">26.20</td>
    <td align="right">33.28</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.03</td>
    <td align="right">15.80</td>
    <td align="right">12.07</td>
    <td align="right">18.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.20</td>
    <td align="right">39.94</td>
    <td align="right">24.74</td>
    <td align="right">38.34</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.91</td>
    <td align="right">58.39</td>
    <td align="right">31.04</td>
    <td align="right">54.52</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.47</td>
    <td align="right">18.46</td>
    <td align="right">13.85</td>
    <td align="right">21.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.05</td>
    <td align="right">5.37</td>
    <td align="right">5.43</td>
    <td align="right">10.37</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.60</td>
    <td align="right">5.76</td>
    <td align="right">5.79</td>
    <td align="right">11.93</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.11</td>
    <td align="right">2.84</td>
    <td align="right">3.22</td>
    <td align="right">9.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.08</td>
    <td align="right">9.08</td>
    <td align="right">8.64</td>
    <td align="right">13.86</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.77</td>
    <td align="right">10.01</td>
    <td align="right">9.80</td>
    <td align="right">16.02</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.69</td>
    <td align="right">4.44</td>
    <td align="right">4.29</td>
    <td align="right">10.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.42</td>
    <td align="right">24.46</td>
    <td align="right">24.20</td>
    <td align="right">28.52</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.02</td>
    <td align="right">28.51</td>
    <td align="right">28.26</td>
    <td align="right">33.15</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.12</td>
    <td align="right">13.54</td>
    <td align="right">13.40</td>
    <td align="right">17.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.41</td>
    <td align="right">36.25</td>
    <td align="right">35.95</td>
    <td align="right">40.35</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.87</td>
    <td align="right">38.16</td>
    <td align="right">38.16</td>
    <td align="right">42.43</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.48</td>
    <td align="right">15.75</td>
    <td align="right">15.59</td>
    <td align="right">20.61</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.06</td>
    <td align="right">7.64</td>
    <td align="right">12.02</td>
    <td align="right">11.92</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.64</td>
    <td align="right">8.25</td>
    <td align="right">13.08</td>
    <td align="right">12.46</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.11</td>
    <td align="right">2.62</td>
    <td align="right">3.13</td>
    <td align="right">9.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.02</td>
    <td align="right">12.09</td>
    <td align="right">13.79</td>
    <td align="right">14.89</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.42</td>
    <td align="right">13.62</td>
    <td align="right">14.28</td>
    <td align="right">17.22</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.71</td>
    <td align="right">5.08</td>
    <td align="right">4.48</td>
    <td align="right">10.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.96</td>
    <td align="right">30.60</td>
    <td align="right">22.79</td>
    <td align="right">30.58</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.25</td>
    <td align="right">31.75</td>
    <td align="right">25.84</td>
    <td align="right">33.11</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.11</td>
    <td align="right">15.77</td>
    <td align="right">11.90</td>
    <td align="right">18.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.23</td>
    <td align="right">47.07</td>
    <td align="right">25.63</td>
    <td align="right">45.21</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.11</td>
    <td align="right">56.81</td>
    <td align="right">30.72</td>
    <td align="right">53.79</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.08</td>
    <td align="right">18.21</td>
    <td align="right">13.54</td>
    <td align="right">21.06</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.04</td>
    <td align="right">9.79</td>
    <td align="right">9.87</td>
    <td align="right">14.15</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.87</td>
    <td align="right">5.69</td>
    <td align="right">5.85</td>
    <td align="right">11.82</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.10</td>
    <td align="right">2.84</td>
    <td align="right">3.18</td>
    <td align="right">9.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.05</td>
    <td align="right">8.99</td>
    <td align="right">8.58</td>
    <td align="right">14.13</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.59</td>
    <td align="right">9.74</td>
    <td align="right">9.86</td>
    <td align="right">15.94</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.80</td>
    <td align="right">4.42</td>
    <td align="right">4.33</td>
    <td align="right">10.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.56</td>
    <td align="right">27.05</td>
    <td align="right">27.06</td>
    <td align="right">31.56</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.05</td>
    <td align="right">32.21</td>
    <td align="right">32.22</td>
    <td align="right">36.87</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.20</td>
    <td align="right">13.47</td>
    <td align="right">13.31</td>
    <td align="right">17.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.28</td>
    <td align="right">35.45</td>
    <td align="right">35.19</td>
    <td align="right">39.67</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.18</td>
    <td align="right">37.64</td>
    <td align="right">37.46</td>
    <td align="right">41.92</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.05</td>
    <td align="right">15.52</td>
    <td align="right">15.26</td>
    <td align="right">20.19</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.11</td>
    <td align="right">2.52</td>
    <td align="right">2.98</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.04</td>
    <td align="right">3.71</td>
    <td align="right">4.08</td>
    <td align="right">11.36</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.13</td>
    <td align="right">3.57</td>
    <td align="right">3.97</td>
    <td align="right">11.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.17</td>
    <td align="right">5.63</td>
    <td align="right">4.71</td>
    <td align="right">11.20</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.86</td>
    <td align="right">11.00</td>
    <td align="right">9.75</td>
    <td align="right">15.96</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.43</td>
    <td align="right">6.75</td>
    <td align="right">6.00</td>
    <td align="right">12.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.05</td>
    <td align="right">17.34</td>
    <td align="right">12.95</td>
    <td align="right">19.61</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.18</td>
    <td align="right">19.43</td>
    <td align="right">16.22</td>
    <td align="right">23.06</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.95</td>
    <td align="right">18.95</td>
    <td align="right">16.04</td>
    <td align="right">22.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.88</td>
    <td align="right">18.26</td>
    <td align="right">13.42</td>
    <td align="right">20.36</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.75</td>
    <td align="right">27.72</td>
    <td align="right">19.32</td>
    <td align="right">27.54</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.79</td>
    <td align="right">27.62</td>
    <td align="right">19.21</td>
    <td align="right">27.05</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.15</td>
    <td align="right">2.66</td>
    <td align="right">3.02</td>
    <td align="right">9.33</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.16</td>
    <td align="right">3.72</td>
    <td align="right">4.11</td>
    <td align="right">11.32</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.13</td>
    <td align="right">3.63</td>
    <td align="right">4.00</td>
    <td align="right">11.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.95</td>
    <td align="right">6.37</td>
    <td align="right">6.09</td>
    <td align="right">11.44</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.90</td>
    <td align="right">12.91</td>
    <td align="right">12.26</td>
    <td align="right">17.91</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.83</td>
    <td align="right">7.01</td>
    <td align="right">7.17</td>
    <td align="right">14.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.33</td>
    <td align="right">14.33</td>
    <td align="right">14.11</td>
    <td align="right">18.57</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.10</td>
    <td align="right">21.49</td>
    <td align="right">20.95</td>
    <td align="right">26.16</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.86</td>
    <td align="right">24.36</td>
    <td align="right">21.92</td>
    <td align="right">27.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.91</td>
    <td align="right">15.71</td>
    <td align="right">15.49</td>
    <td align="right">20.32</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.81</td>
    <td align="right">28.10</td>
    <td align="right">28.00</td>
    <td align="right">33.03</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.80</td>
    <td align="right">28.55</td>
    <td align="right">28.41</td>
    <td align="right">33.13</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.99</td>
    <td align="right">2.46</td>
    <td align="right">2.89</td>
    <td align="right">9.65</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.02</td>
    <td align="right">3.61</td>
    <td align="right">4.02</td>
    <td align="right">11.25</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.55</td>
    <td align="right">3.47</td>
    <td align="right">3.92</td>
    <td align="right">11.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.67</td>
    <td align="right">5.70</td>
    <td align="right">4.82</td>
    <td align="right">11.09</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.95</td>
    <td align="right">5.71</td>
    <td align="right">5.08</td>
    <td align="right">12.34</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.32</td>
    <td align="right">6.53</td>
    <td align="right">5.75</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.16</td>
    <td align="right">15.63</td>
    <td align="right">11.80</td>
    <td align="right">17.89</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.18</td>
    <td align="right">19.62</td>
    <td align="right">16.37</td>
    <td align="right">22.95</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.75</td>
    <td align="right">19.11</td>
    <td align="right">16.09</td>
    <td align="right">22.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">18.02</td>
    <td align="right">18.26</td>
    <td align="right">13.47</td>
    <td align="right">20.49</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.48</td>
    <td align="right">27.54</td>
    <td align="right">19.04</td>
    <td align="right">27.31</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.09</td>
    <td align="right">27.46</td>
    <td align="right">19.16</td>
    <td align="right">27.02</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.97</td>
    <td align="right">2.66</td>
    <td align="right">2.94</td>
    <td align="right">9.26</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">3.97</td>
    <td align="right">3.66</td>
    <td align="right">4.02</td>
    <td align="right">11.23</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.16</td>
    <td align="right">3.55</td>
    <td align="right">3.90</td>
    <td align="right">11.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.64</td>
    <td align="right">4.34</td>
    <td align="right">4.18</td>
    <td align="right">10.00</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.06</td>
    <td align="right">10.17</td>
    <td align="right">9.82</td>
    <td align="right">15.64</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.34</td>
    <td align="right">6.84</td>
    <td align="right">6.79</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.13</td>
    <td align="right">14.97</td>
    <td align="right">14.80</td>
    <td align="right">19.50</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.97</td>
    <td align="right">21.90</td>
    <td align="right">21.70</td>
    <td align="right">26.37</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.79</td>
    <td align="right">21.38</td>
    <td align="right">19.40</td>
    <td align="right">24.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.99</td>
    <td align="right">15.45</td>
    <td align="right">15.27</td>
    <td align="right">19.98</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.41</td>
    <td align="right">28.39</td>
    <td align="right">28.23</td>
    <td align="right">33.09</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.08</td>
    <td align="right">28.10</td>
    <td align="right">27.86</td>
    <td align="right">32.55</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.61</td>
    <td align="right">7.47</td>
    <td align="right">12.22</td>
    <td align="right">12.01</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.65</td>
    <td align="right">10.71</td>
    <td align="right">15.00</td>
    <td align="right">14.22</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.47</td>
    <td align="right">19.13</td>
    <td align="right">19.07</td>
    <td align="right">19.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.25</td>
    <td align="right">12.06</td>
    <td align="right">13.98</td>
    <td align="right">15.43</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.97</td>
    <td align="right">13.47</td>
    <td align="right">14.73</td>
    <td align="right">17.24</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.23</td>
    <td align="right">18.27</td>
    <td align="right">17.97</td>
    <td align="right">19.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.41</td>
    <td align="right">25.61</td>
    <td align="right">19.78</td>
    <td align="right">27.15</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.49</td>
    <td align="right">32.55</td>
    <td align="right">24.12</td>
    <td align="right">34.06</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.17</td>
    <td align="right">44.79</td>
    <td align="right">28.11</td>
    <td align="right">38.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.67</td>
    <td align="right">35.26</td>
    <td align="right">23.54</td>
    <td align="right">37.56</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.11</td>
    <td align="right">41.87</td>
    <td align="right">22.77</td>
    <td align="right">42.24</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.71</td>
    <td align="right">66.29</td>
    <td align="right">37.37</td>
    <td align="right">55.66</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.62</td>
    <td align="right">6.87</td>
    <td align="right">6.50</td>
    <td align="right">11.68</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.87</td>
    <td align="right">9.24</td>
    <td align="right">9.33</td>
    <td align="right">14.56</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.79</td>
    <td align="right">10.03</td>
    <td align="right">10.18</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.41</td>
    <td align="right">9.59</td>
    <td align="right">9.54</td>
    <td align="right">14.87</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.70</td>
    <td align="right">20.20</td>
    <td align="right">19.77</td>
    <td align="right">25.21</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.21</td>
    <td align="right">14.03</td>
    <td align="right">13.88</td>
    <td align="right">19.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.35</td>
    <td align="right">23.77</td>
    <td align="right">23.79</td>
    <td align="right">28.20</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.27</td>
    <td align="right">32.74</td>
    <td align="right">32.19</td>
    <td align="right">36.13</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.07</td>
    <td align="right">39.92</td>
    <td align="right">39.86</td>
    <td align="right">44.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.81</td>
    <td align="right">34.39</td>
    <td align="right">34.28</td>
    <td align="right">37.62</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">44.14</td>
    <td align="right">41.13</td>
    <td align="right">41.90</td>
    <td align="right">44.13</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.05</td>
    <td align="right">64.84</td>
    <td align="right">64.45</td>
    <td align="right">67.83</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.90</td>
    <td align="right">7.76</td>
    <td align="right">12.42</td>
    <td align="right">12.03</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.69</td>
    <td align="right">10.69</td>
    <td align="right">14.94</td>
    <td align="right">14.21</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.27</td>
    <td align="right">19.71</td>
    <td align="right">19.48</td>
    <td align="right">20.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.74</td>
    <td align="right">13.27</td>
    <td align="right">14.32</td>
    <td align="right">16.46</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.09</td>
    <td align="right">13.85</td>
    <td align="right">14.67</td>
    <td align="right">17.32</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">17.06</td>
    <td align="right">18.12</td>
    <td align="right">18.11</td>
    <td align="right">20.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.79</td>
    <td align="right">27.02</td>
    <td align="right">20.29</td>
    <td align="right">28.61</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.55</td>
    <td align="right">32.61</td>
    <td align="right">23.96</td>
    <td align="right">34.02</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.77</td>
    <td align="right">45.55</td>
    <td align="right">19.77</td>
    <td align="right">38.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.35</td>
    <td align="right">43.72</td>
    <td align="right">23.96</td>
    <td align="right">46.04</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.01</td>
    <td align="right">41.90</td>
    <td align="right">22.82</td>
    <td align="right">42.33</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">71.66</td>
    <td align="right">70.30</td>
    <td align="right">26.64</td>
    <td align="right">58.33</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.00</td>
    <td align="right">7.08</td>
    <td align="right">6.71</td>
    <td align="right">12.04</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.86</td>
    <td align="right">8.60</td>
    <td align="right">8.68</td>
    <td align="right">14.12</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.42</td>
    <td align="right">10.34</td>
    <td align="right">10.52</td>
    <td align="right">15.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.76</td>
    <td align="right">10.28</td>
    <td align="right">10.18</td>
    <td align="right">15.85</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.33</td>
    <td align="right">17.66</td>
    <td align="right">16.62</td>
    <td align="right">22.58</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.60</td>
    <td align="right">14.52</td>
    <td align="right">14.59</td>
    <td align="right">19.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.33</td>
    <td align="right">25.08</td>
    <td align="right">24.84</td>
    <td align="right">29.35</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.58</td>
    <td align="right">32.67</td>
    <td align="right">32.48</td>
    <td align="right">36.01</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.61</td>
    <td align="right">40.23</td>
    <td align="right">39.77</td>
    <td align="right">44.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.12</td>
    <td align="right">34.38</td>
    <td align="right">34.31</td>
    <td align="right">37.79</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.03</td>
    <td align="right">41.61</td>
    <td align="right">41.43</td>
    <td align="right">44.32</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">71.73</td>
    <td align="right">68.21</td>
    <td align="right">67.59</td>
    <td align="right">71.39</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.32</td>
    <td align="right">15.61</td>
    <td align="right">7.71</td>
    <td align="right">18.02</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">31.01</td>
    <td align="right">44.21</td>
    <td align="right">37.96</td>
    <td align="right">40.98</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.31</td>
    <td align="right">16.09</td>
    <td align="right">16.32</td>
    <td align="right">23.45</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.60</td>
    <td align="right">17.64</td>
    <td align="right">17.79</td>
    <td align="right">25.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.70</td>
    <td align="right">66.87</td>
    <td align="right">40.65</td>
    <td align="right">55.78</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.36</td>
    <td align="right">18.27</td>
    <td align="right">18.72</td>
    <td align="right">26.35</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.08</td>
    <td align="right">18.98</td>
    <td align="right">18.47</td>
    <td align="right">26.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.81</td>
    <td align="right">81.44</td>
    <td align="right">38.97</td>
    <td align="right">62.37</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.40</td>
    <td align="right">19.69</td>
    <td align="right">19.73</td>
    <td align="right">29.00</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.93</td>
    <td align="right">21.10</td>
    <td align="right">20.90</td>
    <td align="right">28.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.67</td>
    <td align="right">100.51</td>
    <td align="right">41.03</td>
    <td align="right">72.74</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.65</td>
    <td align="right">21.83</td>
    <td align="right">21.82</td>
    <td align="right">30.61</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.12</td>
    <td align="right">21.56</td>
    <td align="right">21.56</td>
    <td align="right">30.33</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.86</td>
    <td align="right">40.57</td>
    <td align="right">41.40</td>
    <td align="right">49.04</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.32</td>
    <td align="right">16.00</td>
    <td align="right">16.35</td>
    <td align="right">23.76</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.58</td>
    <td align="right">17.81</td>
    <td align="right">17.71</td>
    <td align="right">24.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.56</td>
    <td align="right">60.75</td>
    <td align="right">59.96</td>
    <td align="right">69.48</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.31</td>
    <td align="right">18.11</td>
    <td align="right">18.54</td>
    <td align="right">26.40</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.08</td>
    <td align="right">18.97</td>
    <td align="right">18.78</td>
    <td align="right">26.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.24</td>
    <td align="right">71.09</td>
    <td align="right">70.26</td>
    <td align="right">80.48</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.40</td>
    <td align="right">20.29</td>
    <td align="right">19.59</td>
    <td align="right">28.84</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.99</td>
    <td align="right">20.74</td>
    <td align="right">20.55</td>
    <td align="right">28.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.49</td>
    <td align="right">106.96</td>
    <td align="right">112.74</td>
    <td align="right">115.77</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">21.70</td>
    <td align="right">21.80</td>
    <td align="right">30.36</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.25</td>
    <td align="right">22.51</td>
    <td align="right">22.44</td>
    <td align="right">31.42</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.96</td>
    <td align="right">44.43</td>
    <td align="right">38.91</td>
    <td align="right">40.92</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.38</td>
    <td align="right">19.19</td>
    <td align="right">19.19</td>
    <td align="right">27.02</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.61</td>
    <td align="right">22.10</td>
    <td align="right">22.55</td>
    <td align="right">30.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.21</td>
    <td align="right">67.16</td>
    <td align="right">42.05</td>
    <td align="right">54.01</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.49</td>
    <td align="right">23.03</td>
    <td align="right">23.25</td>
    <td align="right">32.43</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.10</td>
    <td align="right">20.82</td>
    <td align="right">20.67</td>
    <td align="right">30.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.44</td>
    <td align="right">82.88</td>
    <td align="right">40.13</td>
    <td align="right">61.82</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.51</td>
    <td align="right">21.17</td>
    <td align="right">20.86</td>
    <td align="right">30.64</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.07</td>
    <td align="right">23.55</td>
    <td align="right">23.61</td>
    <td align="right">32.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">71.74</td>
    <td align="right">103.16</td>
    <td align="right">41.47</td>
    <td align="right">71.58</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.80</td>
    <td align="right">23.95</td>
    <td align="right">24.04</td>
    <td align="right">33.32</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.21</td>
    <td align="right">25.13</td>
    <td align="right">24.81</td>
    <td align="right">34.19</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.94</td>
    <td align="right">46.47</td>
    <td align="right">45.80</td>
    <td align="right">54.64</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.37</td>
    <td align="right">18.87</td>
    <td align="right">19.25</td>
    <td align="right">26.97</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.59</td>
    <td align="right">22.76</td>
    <td align="right">22.55</td>
    <td align="right">30.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.12</td>
    <td align="right">68.91</td>
    <td align="right">66.21</td>
    <td align="right">75.94</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.43</td>
    <td align="right">23.04</td>
    <td align="right">23.23</td>
    <td align="right">32.59</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.09</td>
    <td align="right">20.75</td>
    <td align="right">20.71</td>
    <td align="right">30.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.55</td>
    <td align="right">87.34</td>
    <td align="right">83.76</td>
    <td align="right">95.20</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.54</td>
    <td align="right">21.18</td>
    <td align="right">20.87</td>
    <td align="right">30.54</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.12</td>
    <td align="right">23.61</td>
    <td align="right">23.68</td>
    <td align="right">32.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.02</td>
    <td align="right">112.37</td>
    <td align="right">119.97</td>
    <td align="right">118.40</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.77</td>
    <td align="right">23.96</td>
    <td align="right">23.94</td>
    <td align="right">33.34</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.47</td>
    <td align="right">25.36</td>
    <td align="right">24.81</td>
    <td align="right">34.19</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.99</td>
    <td align="right">23.74</td>
    <td align="right">27.54</td>
    <td align="right">28.07</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.28</td>
    <td align="right">27.31</td>
    <td align="right">29.28</td>
    <td align="right">30.57</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.93</td>
    <td align="right">15.12</td>
    <td align="right">24.24</td>
    <td align="right">22.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.74</td>
    <td align="right">30.46</td>
    <td align="right">28.41</td>
    <td align="right">31.83</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.13</td>
    <td align="right">34.37</td>
    <td align="right">33.91</td>
    <td align="right">35.73</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.17</td>
    <td align="right">19.23</td>
    <td align="right">26.60</td>
    <td align="right">24.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.36</td>
    <td align="right">43.90</td>
    <td align="right">30.53</td>
    <td align="right">39.91</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.46</td>
    <td align="right">49.67</td>
    <td align="right">40.05</td>
    <td align="right">45.04</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.02</td>
    <td align="right">21.62</td>
    <td align="right">27.34</td>
    <td align="right">28.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.66</td>
    <td align="right">47.95</td>
    <td align="right">29.94</td>
    <td align="right">42.56</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.56</td>
    <td align="right">57.25</td>
    <td align="right">42.25</td>
    <td align="right">49.25</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.03</td>
    <td align="right">29.25</td>
    <td align="right">26.62</td>
    <td align="right">31.08</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.73</td>
    <td align="right">24.00</td>
    <td align="right">23.91</td>
    <td align="right">30.54</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.26</td>
    <td align="right">26.79</td>
    <td align="right">26.80</td>
    <td align="right">32.72</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.76</td>
    <td align="right">16.27</td>
    <td align="right">16.76</td>
    <td align="right">23.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.44</td>
    <td align="right">30.13</td>
    <td align="right">29.69</td>
    <td align="right">34.11</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.12</td>
    <td align="right">35.18</td>
    <td align="right">34.80</td>
    <td align="right">39.48</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.91</td>
    <td align="right">18.72</td>
    <td align="right">18.25</td>
    <td align="right">26.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.18</td>
    <td align="right">37.70</td>
    <td align="right">37.48</td>
    <td align="right">41.69</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.92</td>
    <td align="right">49.55</td>
    <td align="right">49.20</td>
    <td align="right">54.17</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.03</td>
    <td align="right">21.38</td>
    <td align="right">20.66</td>
    <td align="right">28.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">42.32</td>
    <td align="right">41.91</td>
    <td align="right">46.27</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.49</td>
    <td align="right">58.58</td>
    <td align="right">58.40</td>
    <td align="right">63.46</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.86</td>
    <td align="right">26.09</td>
    <td align="right">26.15</td>
    <td align="right">32.65</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.87</td>
    <td align="right">23.82</td>
    <td align="right">27.02</td>
    <td align="right">27.93</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.29</td>
    <td align="right">27.34</td>
    <td align="right">29.31</td>
    <td align="right">31.27</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.81</td>
    <td align="right">15.09</td>
    <td align="right">24.20</td>
    <td align="right">21.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.91</td>
    <td align="right">30.91</td>
    <td align="right">28.27</td>
    <td align="right">31.97</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.04</td>
    <td align="right">34.40</td>
    <td align="right">34.14</td>
    <td align="right">35.63</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.02</td>
    <td align="right">19.24</td>
    <td align="right">26.53</td>
    <td align="right">24.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.96</td>
    <td align="right">43.18</td>
    <td align="right">31.19</td>
    <td align="right">39.77</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.36</td>
    <td align="right">49.81</td>
    <td align="right">40.04</td>
    <td align="right">45.12</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.55</td>
    <td align="right">21.61</td>
    <td align="right">27.39</td>
    <td align="right">26.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.50</td>
    <td align="right">49.34</td>
    <td align="right">29.78</td>
    <td align="right">42.46</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.41</td>
    <td align="right">57.68</td>
    <td align="right">41.55</td>
    <td align="right">49.26</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.02</td>
    <td align="right">29.18</td>
    <td align="right">27.25</td>
    <td align="right">31.01</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.89</td>
    <td align="right">23.67</td>
    <td align="right">23.73</td>
    <td align="right">30.19</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.24</td>
    <td align="right">26.78</td>
    <td align="right">27.04</td>
    <td align="right">32.68</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.93</td>
    <td align="right">16.46</td>
    <td align="right">16.44</td>
    <td align="right">24.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.81</td>
    <td align="right">32.27</td>
    <td align="right">31.98</td>
    <td align="right">36.19</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.02</td>
    <td align="right">35.34</td>
    <td align="right">34.81</td>
    <td align="right">39.49</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.91</td>
    <td align="right">19.20</td>
    <td align="right">18.65</td>
    <td align="right">25.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.02</td>
    <td align="right">38.50</td>
    <td align="right">38.14</td>
    <td align="right">42.18</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.39</td>
    <td align="right">49.45</td>
    <td align="right">49.35</td>
    <td align="right">53.96</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.57</td>
    <td align="right">21.94</td>
    <td align="right">21.17</td>
    <td align="right">29.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.51</td>
    <td align="right">43.98</td>
    <td align="right">43.52</td>
    <td align="right">47.40</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.54</td>
    <td align="right">58.60</td>
    <td align="right">58.32</td>
    <td align="right">63.41</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.07</td>
    <td align="right">26.47</td>
    <td align="right">26.10</td>
    <td align="right">32.56</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.49</td>
    <td align="right">16.69</td>
    <td align="right">24.69</td>
    <td align="right">23.43</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.75</td>
    <td align="right">23.66</td>
    <td align="right">27.12</td>
    <td align="right">28.04</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.29</td>
    <td align="right">27.55</td>
    <td align="right">29.32</td>
    <td align="right">30.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.04</td>
    <td align="right">20.02</td>
    <td align="right">26.57</td>
    <td align="right">26.32</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.66</td>
    <td align="right">30.49</td>
    <td align="right">28.40</td>
    <td align="right">31.80</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.14</td>
    <td align="right">34.40</td>
    <td align="right">33.93</td>
    <td align="right">35.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.63</td>
    <td align="right">22.92</td>
    <td align="right">28.21</td>
    <td align="right">28.09</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.14</td>
    <td align="right">43.86</td>
    <td align="right">30.85</td>
    <td align="right">40.36</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.45</td>
    <td align="right">49.67</td>
    <td align="right">40.09</td>
    <td align="right">44.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.97</td>
    <td align="right">30.87</td>
    <td align="right">28.97</td>
    <td align="right">32.69</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">38.06</td>
    <td align="right">48.23</td>
    <td align="right">29.87</td>
    <td align="right">42.41</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.54</td>
    <td align="right">57.24</td>
    <td align="right">42.13</td>
    <td align="right">49.25</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.47</td>
    <td align="right">17.40</td>
    <td align="right">17.34</td>
    <td align="right">24.57</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.96</td>
    <td align="right">23.93</td>
    <td align="right">23.94</td>
    <td align="right">30.47</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">26.79</td>
    <td align="right">26.87</td>
    <td align="right">32.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.04</td>
    <td align="right">21.89</td>
    <td align="right">21.26</td>
    <td align="right">27.98</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.50</td>
    <td align="right">29.69</td>
    <td align="right">29.74</td>
    <td align="right">34.01</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.13</td>
    <td align="right">35.19</td>
    <td align="right">34.79</td>
    <td align="right">39.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.60</td>
    <td align="right">24.53</td>
    <td align="right">24.19</td>
    <td align="right">31.41</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.16</td>
    <td align="right">37.70</td>
    <td align="right">37.42</td>
    <td align="right">41.55</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.88</td>
    <td align="right">49.53</td>
    <td align="right">49.22</td>
    <td align="right">53.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">32.04</td>
    <td align="right">34.48</td>
    <td align="right">34.12</td>
    <td align="right">39.39</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.80</td>
    <td align="right">42.33</td>
    <td align="right">41.98</td>
    <td align="right">46.43</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.51</td>
    <td align="right">58.62</td>
    <td align="right">58.40</td>
    <td align="right">63.15</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.51</td>
    <td align="right">16.63</td>
    <td align="right">24.57</td>
    <td align="right">23.39</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.95</td>
    <td align="right">23.79</td>
    <td align="right">27.01</td>
    <td align="right">27.86</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">28.15</td>
    <td align="right">29.27</td>
    <td align="right">30.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.11</td>
    <td align="right">20.04</td>
    <td align="right">26.59</td>
    <td align="right">25.99</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.06</td>
    <td align="right">30.47</td>
    <td align="right">28.41</td>
    <td align="right">31.95</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.04</td>
    <td align="right">34.39</td>
    <td align="right">34.13</td>
    <td align="right">35.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.52</td>
    <td align="right">22.89</td>
    <td align="right">28.60</td>
    <td align="right">28.33</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.89</td>
    <td align="right">43.70</td>
    <td align="right">30.55</td>
    <td align="right">39.78</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.38</td>
    <td align="right">49.72</td>
    <td align="right">40.00</td>
    <td align="right">45.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.99</td>
    <td align="right">30.96</td>
    <td align="right">28.69</td>
    <td align="right">33.16</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">49.51</td>
    <td align="right">29.76</td>
    <td align="right">42.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.32</td>
    <td align="right">57.60</td>
    <td align="right">41.50</td>
    <td align="right">49.63</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.51</td>
    <td align="right">17.71</td>
    <td align="right">17.28</td>
    <td align="right">23.93</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.93</td>
    <td align="right">23.75</td>
    <td align="right">23.67</td>
    <td align="right">30.40</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.24</td>
    <td align="right">26.82</td>
    <td align="right">26.84</td>
    <td align="right">32.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.08</td>
    <td align="right">21.59</td>
    <td align="right">21.22</td>
    <td align="right">28.19</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.79</td>
    <td align="right">32.31</td>
    <td align="right">31.97</td>
    <td align="right">36.14</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">35.39</td>
    <td align="right">34.80</td>
    <td align="right">39.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.51</td>
    <td align="right">24.56</td>
    <td align="right">24.22</td>
    <td align="right">31.23</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.88</td>
    <td align="right">38.49</td>
    <td align="right">38.14</td>
    <td align="right">42.18</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.37</td>
    <td align="right">49.45</td>
    <td align="right">49.37</td>
    <td align="right">54.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.88</td>
    <td align="right">34.48</td>
    <td align="right">34.13</td>
    <td align="right">39.27</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.57</td>
    <td align="right">43.95</td>
    <td align="right">43.54</td>
    <td align="right">47.66</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.50</td>
    <td align="right">58.59</td>
    <td align="right">58.40</td>
    <td align="right">63.47</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.34</td>
    <td align="right">24.90</td>
    <td align="right">28.08</td>
    <td align="right">29.08</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.68</td>
    <td align="right">31.73</td>
    <td align="right">36.45</td>
    <td align="right">34.62</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.32</td>
    <td align="right">37.07</td>
    <td align="right">34.00</td>
    <td align="right">35.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.39</td>
    <td align="right">37.54</td>
    <td align="right">28.44</td>
    <td align="right">36.42</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.46</td>
    <td align="right">41.28</td>
    <td align="right">34.72</td>
    <td align="right">39.84</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.36</td>
    <td align="right">47.58</td>
    <td align="right">36.43</td>
    <td align="right">41.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.06</td>
    <td align="right">44.15</td>
    <td align="right">28.27</td>
    <td align="right">40.15</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.58</td>
    <td align="right">50.11</td>
    <td align="right">35.93</td>
    <td align="right">44.53</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.86</td>
    <td align="right">52.27</td>
    <td align="right">32.34</td>
    <td align="right">43.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.29</td>
    <td align="right">49.77</td>
    <td align="right">29.62</td>
    <td align="right">42.82</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.49</td>
    <td align="right">52.75</td>
    <td align="right">35.73</td>
    <td align="right">46.14</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.98</td>
    <td align="right">65.71</td>
    <td align="right">35.12</td>
    <td align="right">52.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.34</td>
    <td align="right">24.58</td>
    <td align="right">24.36</td>
    <td align="right">30.46</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.68</td>
    <td align="right">32.78</td>
    <td align="right">32.72</td>
    <td align="right">37.52</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.20</td>
    <td align="right">35.17</td>
    <td align="right">34.98</td>
    <td align="right">40.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.39</td>
    <td align="right">34.01</td>
    <td align="right">33.62</td>
    <td align="right">38.59</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.41</td>
    <td align="right">39.97</td>
    <td align="right">39.70</td>
    <td align="right">45.16</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">40.73</td>
    <td align="right">44.56</td>
    <td align="right">44.29</td>
    <td align="right">49.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.08</td>
    <td align="right">41.51</td>
    <td align="right">41.11</td>
    <td align="right">46.24</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.58</td>
    <td align="right">49.76</td>
    <td align="right">49.18</td>
    <td align="right">54.13</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.34</td>
    <td align="right">48.04</td>
    <td align="right">47.44</td>
    <td align="right">53.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.30</td>
    <td align="right">47.40</td>
    <td align="right">47.34</td>
    <td align="right">51.82</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.46</td>
    <td align="right">52.98</td>
    <td align="right">52.72</td>
    <td align="right">57.37</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.97</td>
    <td align="right">64.80</td>
    <td align="right">64.74</td>
    <td align="right">72.90</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.31</td>
    <td align="right">24.36</td>
    <td align="right">28.09</td>
    <td align="right">28.42</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.08</td>
    <td align="right">31.83</td>
    <td align="right">36.38</td>
    <td align="right">34.28</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.47</td>
    <td align="right">37.75</td>
    <td align="right">34.36</td>
    <td align="right">35.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.38</td>
    <td align="right">37.56</td>
    <td align="right">28.41</td>
    <td align="right">36.36</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.32</td>
    <td align="right">40.96</td>
    <td align="right">34.79</td>
    <td align="right">39.51</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.30</td>
    <td align="right">47.42</td>
    <td align="right">36.96</td>
    <td align="right">42.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.12</td>
    <td align="right">44.13</td>
    <td align="right">28.11</td>
    <td align="right">40.10</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.54</td>
    <td align="right">50.26</td>
    <td align="right">36.18</td>
    <td align="right">44.78</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.37</td>
    <td align="right">51.22</td>
    <td align="right">33.65</td>
    <td align="right">45.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.30</td>
    <td align="right">49.75</td>
    <td align="right">29.60</td>
    <td align="right">42.81</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.44</td>
    <td align="right">53.24</td>
    <td align="right">36.06</td>
    <td align="right">46.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.04</td>
    <td align="right">65.52</td>
    <td align="right">33.45</td>
    <td align="right">51.74</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.45</td>
    <td align="right">26.12</td>
    <td align="right">24.66</td>
    <td align="right">30.27</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.12</td>
    <td align="right">32.79</td>
    <td align="right">32.68</td>
    <td align="right">37.53</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">30.00</td>
    <td align="right">35.23</td>
    <td align="right">35.33</td>
    <td align="right">41.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.42</td>
    <td align="right">33.74</td>
    <td align="right">33.44</td>
    <td align="right">38.29</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.30</td>
    <td align="right">39.95</td>
    <td align="right">39.68</td>
    <td align="right">45.20</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">41.49</td>
    <td align="right">46.21</td>
    <td align="right">45.03</td>
    <td align="right">50.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.13</td>
    <td align="right">41.64</td>
    <td align="right">41.11</td>
    <td align="right">45.99</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.58</td>
    <td align="right">49.69</td>
    <td align="right">49.20</td>
    <td align="right">54.15</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.31</td>
    <td align="right">49.15</td>
    <td align="right">48.96</td>
    <td align="right">56.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.30</td>
    <td align="right">47.15</td>
    <td align="right">47.25</td>
    <td align="right">51.32</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.46</td>
    <td align="right">52.97</td>
    <td align="right">53.25</td>
    <td align="right">57.57</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.03</td>
    <td align="right">67.93</td>
    <td align="right">67.77</td>
    <td align="right">74.53</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.28</td>
    <td align="right">69.56</td>
    <td align="right">22.12</td>
    <td align="right">55.86</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">35.18</td>
    <td align="right">50.15</td>
    <td align="right">43.31</td>
    <td align="right">48.60</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.43</td>
    <td align="right">17.30</td>
    <td align="right">17.73</td>
    <td align="right">25.73</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">16.66</td>
    <td align="right">20.07</td>
    <td align="right">20.35</td>
    <td align="right">28.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">101.92</td>
    <td align="right">132.63</td>
    <td align="right">60.51</td>
    <td align="right">96.99</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.12</td>
    <td align="right">29.07</td>
    <td align="right">29.12</td>
    <td align="right">37.48</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">25.85</td>
    <td align="right">28.60</td>
    <td align="right">28.58</td>
    <td align="right">38.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">188.34</td>
    <td align="right">243.17</td>
    <td align="right">76.71</td>
    <td align="right">160.42</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.06</td>
    <td align="right">47.30</td>
    <td align="right">47.07</td>
    <td align="right">58.10</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.66</td>
    <td align="right">49.13</td>
    <td align="right">49.77</td>
    <td align="right">58.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.13</td>
    <td align="right">402.08</td>
    <td align="right">98.78</td>
    <td align="right">250.15</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.04</td>
    <td align="right">63.47</td>
    <td align="right">63.76</td>
    <td align="right">72.97</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.21</td>
    <td align="right">64.43</td>
    <td align="right">64.54</td>
    <td align="right">73.94</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">34.55</td>
    <td align="right">43.53</td>
    <td align="right">44.06</td>
    <td align="right">52.16</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.44</td>
    <td align="right">20.36</td>
    <td align="right">19.61</td>
    <td align="right">28.21</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">16.03</td>
    <td align="right">18.53</td>
    <td align="right">19.22</td>
    <td align="right">27.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">100.74</td>
    <td align="right">113.89</td>
    <td align="right">109.30</td>
    <td align="right">121.26</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.84</td>
    <td align="right">28.40</td>
    <td align="right">28.37</td>
    <td align="right">35.94</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.26</td>
    <td align="right">31.37</td>
    <td align="right">30.47</td>
    <td align="right">39.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">191.04</td>
    <td align="right">179.83</td>
    <td align="right">175.22</td>
    <td align="right">204.02</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.13</td>
    <td align="right">49.12</td>
    <td align="right">49.50</td>
    <td align="right">59.83</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.99</td>
    <td align="right">49.37</td>
    <td align="right">49.12</td>
    <td align="right">58.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.77</td>
    <td align="right">408.51</td>
    <td align="right">412.01</td>
    <td align="right">414.20</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.85</td>
    <td align="right">61.38</td>
    <td align="right">61.64</td>
    <td align="right">70.53</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.01</td>
    <td align="right">65.64</td>
    <td align="right">64.74</td>
    <td align="right">74.01</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">42.38</td>
    <td align="right">58.85</td>
    <td align="right">47.91</td>
    <td align="right">53.12</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.77</td>
    <td align="right">22.96</td>
    <td align="right">22.16</td>
    <td align="right">30.51</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.53</td>
    <td align="right">27.49</td>
    <td align="right">27.88</td>
    <td align="right">36.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">97.32</td>
    <td align="right">128.84</td>
    <td align="right">61.05</td>
    <td align="right">94.41</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.90</td>
    <td align="right">37.63</td>
    <td align="right">37.60</td>
    <td align="right">47.14</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.41</td>
    <td align="right">32.80</td>
    <td align="right">32.48</td>
    <td align="right">43.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">188.64</td>
    <td align="right">250.25</td>
    <td align="right">78.44</td>
    <td align="right">164.83</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.13</td>
    <td align="right">47.84</td>
    <td align="right">47.70</td>
    <td align="right">58.60</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.23</td>
    <td align="right">51.84</td>
    <td align="right">51.78</td>
    <td align="right">61.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">295.37</td>
    <td align="right">404.26</td>
    <td align="right">98.82</td>
    <td align="right">272.76</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.84</td>
    <td align="right">64.18</td>
    <td align="right">64.19</td>
    <td align="right">73.84</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.82</td>
    <td align="right">68.56</td>
    <td align="right">68.36</td>
    <td align="right">77.87</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">39.82</td>
    <td align="right">55.84</td>
    <td align="right">54.72</td>
    <td align="right">64.51</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.03</td>
    <td align="right">23.30</td>
    <td align="right">23.52</td>
    <td align="right">30.84</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.26</td>
    <td align="right">27.09</td>
    <td align="right">27.60</td>
    <td align="right">36.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">101.66</td>
    <td align="right">122.93</td>
    <td align="right">115.18</td>
    <td align="right">128.65</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.06</td>
    <td align="right">34.09</td>
    <td align="right">34.06</td>
    <td align="right">43.96</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.88</td>
    <td align="right">34.25</td>
    <td align="right">34.01</td>
    <td align="right">45.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.66</td>
    <td align="right">206.87</td>
    <td align="right">193.51</td>
    <td align="right">212.73</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.92</td>
    <td align="right">47.58</td>
    <td align="right">47.30</td>
    <td align="right">58.03</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.04</td>
    <td align="right">53.00</td>
    <td align="right">53.14</td>
    <td align="right">62.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.59</td>
    <td align="right">406.37</td>
    <td align="right">409.08</td>
    <td align="right">411.21</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.84</td>
    <td align="right">63.87</td>
    <td align="right">63.86</td>
    <td align="right">73.58</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.62</td>
    <td align="right">68.93</td>
    <td align="right">68.74</td>
    <td align="right">78.32</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.32</td>
    <td align="right">27.72</td>
    <td align="right">30.04</td>
    <td align="right">32.96</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.87</td>
    <td align="right">33.38</td>
    <td align="right">32.15</td>
    <td align="right">36.93</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.00</td>
    <td align="right">16.32</td>
    <td align="right">26.30</td>
    <td align="right">23.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.23</td>
    <td align="right">43.21</td>
    <td align="right">37.30</td>
    <td align="right">44.57</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.57</td>
    <td align="right">52.77</td>
    <td align="right">45.91</td>
    <td align="right">53.24</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.53</td>
    <td align="right">30.76</td>
    <td align="right">36.07</td>
    <td align="right">34.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.37</td>
    <td align="right">77.87</td>
    <td align="right">50.02</td>
    <td align="right">71.07</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.26</td>
    <td align="right">84.18</td>
    <td align="right">67.51</td>
    <td align="right">78.24</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.69</td>
    <td align="right">46.11</td>
    <td align="right">46.78</td>
    <td align="right">48.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.51</td>
    <td align="right">99.50</td>
    <td align="right">57.19</td>
    <td align="right">90.05</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.24</td>
    <td align="right">107.65</td>
    <td align="right">87.21</td>
    <td align="right">97.28</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.96</td>
    <td align="right">75.03</td>
    <td align="right">53.02</td>
    <td align="right">72.53</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.46</td>
    <td align="right">28.69</td>
    <td align="right">28.83</td>
    <td align="right">36.21</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.30</td>
    <td align="right">31.93</td>
    <td align="right">31.93</td>
    <td align="right">38.33</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.91</td>
    <td align="right">20.18</td>
    <td align="right">21.49</td>
    <td align="right">26.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">38.71</td>
    <td align="right">42.41</td>
    <td align="right">42.51</td>
    <td align="right">46.83</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.16</td>
    <td align="right">52.52</td>
    <td align="right">52.27</td>
    <td align="right">57.19</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.55</td>
    <td align="right">29.75</td>
    <td align="right">29.23</td>
    <td align="right">37.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.27</td>
    <td align="right">70.75</td>
    <td align="right">70.51</td>
    <td align="right">74.91</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.49</td>
    <td align="right">83.42</td>
    <td align="right">83.09</td>
    <td align="right">87.78</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.56</td>
    <td align="right">45.49</td>
    <td align="right">44.89</td>
    <td align="right">51.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.64</td>
    <td align="right">95.12</td>
    <td align="right">94.76</td>
    <td align="right">99.79</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.06</td>
    <td align="right">110.58</td>
    <td align="right">110.45</td>
    <td align="right">115.17</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.41</td>
    <td align="right">74.52</td>
    <td align="right">74.64</td>
    <td align="right">81.64</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.61</td>
    <td align="right">27.88</td>
    <td align="right">30.65</td>
    <td align="right">33.08</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.35</td>
    <td align="right">33.77</td>
    <td align="right">32.37</td>
    <td align="right">37.25</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.65</td>
    <td align="right">18.98</td>
    <td align="right">27.06</td>
    <td align="right">24.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.24</td>
    <td align="right">44.71</td>
    <td align="right">37.46</td>
    <td align="right">46.17</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.56</td>
    <td align="right">50.21</td>
    <td align="right">45.61</td>
    <td align="right">51.87</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.59</td>
    <td align="right">28.11</td>
    <td align="right">34.14</td>
    <td align="right">33.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.80</td>
    <td align="right">75.59</td>
    <td align="right">49.25</td>
    <td align="right">68.81</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.43</td>
    <td align="right">82.85</td>
    <td align="right">66.41</td>
    <td align="right">76.95</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.67</td>
    <td align="right">46.55</td>
    <td align="right">46.83</td>
    <td align="right">49.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.34</td>
    <td align="right">98.78</td>
    <td align="right">56.72</td>
    <td align="right">87.87</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.39</td>
    <td align="right">110.11</td>
    <td align="right">88.03</td>
    <td align="right">99.90</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.84</td>
    <td align="right">76.02</td>
    <td align="right">53.47</td>
    <td align="right">73.24</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.07</td>
    <td align="right">26.19</td>
    <td align="right">26.26</td>
    <td align="right">33.69</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.54</td>
    <td align="right">32.20</td>
    <td align="right">32.29</td>
    <td align="right">38.56</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">13.92</td>
    <td align="right">18.07</td>
    <td align="right">18.12</td>
    <td align="right">26.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.80</td>
    <td align="right">44.59</td>
    <td align="right">44.35</td>
    <td align="right">48.19</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.45</td>
    <td align="right">51.98</td>
    <td align="right">49.99</td>
    <td align="right">55.04</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.00</td>
    <td align="right">29.32</td>
    <td align="right">28.63</td>
    <td align="right">35.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.81</td>
    <td align="right">73.35</td>
    <td align="right">72.81</td>
    <td align="right">76.95</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.20</td>
    <td align="right">83.81</td>
    <td align="right">83.64</td>
    <td align="right">88.73</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.43</td>
    <td align="right">45.92</td>
    <td align="right">45.13</td>
    <td align="right">51.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.57</td>
    <td align="right">98.39</td>
    <td align="right">97.99</td>
    <td align="right">101.20</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.95</td>
    <td align="right">109.11</td>
    <td align="right">108.94</td>
    <td align="right">113.69</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.31</td>
    <td align="right">76.04</td>
    <td align="right">75.96</td>
    <td align="right">82.61</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.12</td>
    <td align="right">19.56</td>
    <td align="right">28.80</td>
    <td align="right">26.99</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">21.73</td>
    <td align="right">26.32</td>
    <td align="right">29.37</td>
    <td align="right">31.52</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.32</td>
    <td align="right">33.71</td>
    <td align="right">32.61</td>
    <td align="right">37.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.51</td>
    <td align="right">31.71</td>
    <td align="right">39.41</td>
    <td align="right">38.06</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.10</td>
    <td align="right">45.88</td>
    <td align="right">39.42</td>
    <td align="right">47.43</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.82</td>
    <td align="right">52.91</td>
    <td align="right">46.07</td>
    <td align="right">53.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.90</td>
    <td align="right">47.73</td>
    <td align="right">50.26</td>
    <td align="right">50.53</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.22</td>
    <td align="right">77.68</td>
    <td align="right">49.44</td>
    <td align="right">69.27</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.10</td>
    <td align="right">83.13</td>
    <td align="right">67.13</td>
    <td align="right">77.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.21</td>
    <td align="right">82.01</td>
    <td align="right">59.62</td>
    <td align="right">79.80</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.71</td>
    <td align="right">98.10</td>
    <td align="right">55.86</td>
    <td align="right">86.32</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.08</td>
    <td align="right">107.57</td>
    <td align="right">86.57</td>
    <td align="right">97.24</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.86</td>
    <td align="right">20.34</td>
    <td align="right">20.25</td>
    <td align="right">29.72</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.62</td>
    <td align="right">28.92</td>
    <td align="right">28.90</td>
    <td align="right">36.22</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.73</td>
    <td align="right">31.38</td>
    <td align="right">32.09</td>
    <td align="right">37.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.58</td>
    <td align="right">32.54</td>
    <td align="right">32.26</td>
    <td align="right">38.60</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.20</td>
    <td align="right">44.38</td>
    <td align="right">44.33</td>
    <td align="right">48.68</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">52.53</td>
    <td align="right">51.79</td>
    <td align="right">51.23</td>
    <td align="right">56.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.69</td>
    <td align="right">55.94</td>
    <td align="right">54.92</td>
    <td align="right">62.29</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.56</td>
    <td align="right">71.99</td>
    <td align="right">72.49</td>
    <td align="right">76.88</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.14</td>
    <td align="right">83.14</td>
    <td align="right">82.88</td>
    <td align="right">87.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.45</td>
    <td align="right">86.61</td>
    <td align="right">86.29</td>
    <td align="right">91.70</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.90</td>
    <td align="right">93.10</td>
    <td align="right">92.73</td>
    <td align="right">97.24</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.37</td>
    <td align="right">109.82</td>
    <td align="right">109.73</td>
    <td align="right">114.05</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.79</td>
    <td align="right">18.30</td>
    <td align="right">27.66</td>
    <td align="right">26.57</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.44</td>
    <td align="right">27.83</td>
    <td align="right">30.03</td>
    <td align="right">33.08</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.18</td>
    <td align="right">33.62</td>
    <td align="right">32.50</td>
    <td align="right">36.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.65</td>
    <td align="right">30.81</td>
    <td align="right">38.16</td>
    <td align="right">36.30</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.10</td>
    <td align="right">44.27</td>
    <td align="right">37.57</td>
    <td align="right">45.76</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.01</td>
    <td align="right">48.69</td>
    <td align="right">44.58</td>
    <td align="right">50.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.43</td>
    <td align="right">47.09</td>
    <td align="right">51.44</td>
    <td align="right">51.25</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.31</td>
    <td align="right">77.22</td>
    <td align="right">51.19</td>
    <td align="right">69.98</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.08</td>
    <td align="right">84.31</td>
    <td align="right">67.40</td>
    <td align="right">78.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.89</td>
    <td align="right">79.78</td>
    <td align="right">58.80</td>
    <td align="right">77.79</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.92</td>
    <td align="right">98.39</td>
    <td align="right">56.19</td>
    <td align="right">88.08</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.07</td>
    <td align="right">109.91</td>
    <td align="right">87.45</td>
    <td align="right">99.06</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.59</td>
    <td align="right">18.82</td>
    <td align="right">19.31</td>
    <td align="right">28.07</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.59</td>
    <td align="right">27.10</td>
    <td align="right">26.99</td>
    <td align="right">34.52</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.15</td>
    <td align="right">31.80</td>
    <td align="right">31.94</td>
    <td align="right">38.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.32</td>
    <td align="right">32.34</td>
    <td align="right">31.80</td>
    <td align="right">39.05</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.49</td>
    <td align="right">41.64</td>
    <td align="right">41.19</td>
    <td align="right">45.32</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.64</td>
    <td align="right">50.28</td>
    <td align="right">48.23</td>
    <td align="right">53.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.75</td>
    <td align="right">55.29</td>
    <td align="right">54.20</td>
    <td align="right">62.15</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.88</td>
    <td align="right">75.71</td>
    <td align="right">75.35</td>
    <td align="right">79.46</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.94</td>
    <td align="right">83.52</td>
    <td align="right">83.39</td>
    <td align="right">88.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.24</td>
    <td align="right">84.58</td>
    <td align="right">84.30</td>
    <td align="right">89.54</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.17</td>
    <td align="right">97.06</td>
    <td align="right">96.65</td>
    <td align="right">99.89</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.38</td>
    <td align="right">110.37</td>
    <td align="right">110.32</td>
    <td align="right">114.75</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.86</td>
    <td align="right">29.08</td>
    <td align="right">31.76</td>
    <td align="right">33.74</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.20</td>
    <td align="right">38.21</td>
    <td align="right">41.17</td>
    <td align="right">41.66</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">37.13</td>
    <td align="right">44.31</td>
    <td align="right">39.65</td>
    <td align="right">43.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.64</td>
    <td align="right">49.11</td>
    <td align="right">38.35</td>
    <td align="right">47.91</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.31</td>
    <td align="right">60.87</td>
    <td align="right">47.55</td>
    <td align="right">58.67</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">62.69</td>
    <td align="right">70.33</td>
    <td align="right">45.94</td>
    <td align="right">61.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.15</td>
    <td align="right">72.42</td>
    <td align="right">47.03</td>
    <td align="right">68.17</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.46</td>
    <td align="right">87.24</td>
    <td align="right">59.16</td>
    <td align="right">79.05</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.98</td>
    <td align="right">94.07</td>
    <td align="right">43.07</td>
    <td align="right">77.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.36</td>
    <td align="right">91.13</td>
    <td align="right">58.68</td>
    <td align="right">84.84</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.67</td>
    <td align="right">106.37</td>
    <td align="right">68.10</td>
    <td align="right">95.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">141.28</td>
    <td align="right">141.67</td>
    <td align="right">51.29</td>
    <td align="right">111.24</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">22.41</td>
    <td align="right">29.67</td>
    <td align="right">29.26</td>
    <td align="right">35.98</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">38.98</td>
    <td align="right">40.23</td>
    <td align="right">41.46</td>
    <td align="right">46.74</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.08</td>
    <td align="right">40.67</td>
    <td align="right">40.49</td>
    <td align="right">45.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.47</td>
    <td align="right">47.92</td>
    <td align="right">47.36</td>
    <td align="right">51.89</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">58.44</td>
    <td align="right">57.31</td>
    <td align="right">57.06</td>
    <td align="right">63.80</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">64.61</td>
    <td align="right">68.82</td>
    <td align="right">68.46</td>
    <td align="right">73.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.40</td>
    <td align="right">69.53</td>
    <td align="right">68.91</td>
    <td align="right">73.83</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.17</td>
    <td align="right">90.09</td>
    <td align="right">89.62</td>
    <td align="right">94.27</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.37</td>
    <td align="right">93.32</td>
    <td align="right">92.80</td>
    <td align="right">98.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.36</td>
    <td align="right">89.51</td>
    <td align="right">88.60</td>
    <td align="right">91.83</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.62</td>
    <td align="right">105.78</td>
    <td align="right">105.64</td>
    <td align="right">110.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">139.60</td>
    <td align="right">140.28</td>
    <td align="right">139.89</td>
    <td align="right">147.73</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.88</td>
    <td align="right">29.05</td>
    <td align="right">31.60</td>
    <td align="right">33.80</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.35</td>
    <td align="right">39.36</td>
    <td align="right">41.14</td>
    <td align="right">40.25</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.41</td>
    <td align="right">41.76</td>
    <td align="right">38.24</td>
    <td align="right">42.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.36</td>
    <td align="right">52.26</td>
    <td align="right">37.73</td>
    <td align="right">51.04</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">59.25</td>
    <td align="right">55.11</td>
    <td align="right">44.96</td>
    <td align="right">53.04</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.05</td>
    <td align="right">70.40</td>
    <td align="right">46.78</td>
    <td align="right">61.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.20</td>
    <td align="right">71.99</td>
    <td align="right">46.62</td>
    <td align="right">67.40</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.67</td>
    <td align="right">89.95</td>
    <td align="right">61.23</td>
    <td align="right">81.69</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.79</td>
    <td align="right">95.13</td>
    <td align="right">44.96</td>
    <td align="right">79.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.82</td>
    <td align="right">90.36</td>
    <td align="right">57.54</td>
    <td align="right">83.77</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.26</td>
    <td align="right">106.83</td>
    <td align="right">68.54</td>
    <td align="right">95.50</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">141.27</td>
    <td align="right">143.79</td>
    <td align="right">51.37</td>
    <td align="right">110.98</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.13</td>
    <td align="right">27.51</td>
    <td align="right">27.22</td>
    <td align="right">34.16</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.16</td>
    <td align="right">38.55</td>
    <td align="right">38.93</td>
    <td align="right">44.21</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.93</td>
    <td align="right">39.82</td>
    <td align="right">39.59</td>
    <td align="right">46.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.60</td>
    <td align="right">46.38</td>
    <td align="right">45.94</td>
    <td align="right">50.58</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">58.75</td>
    <td align="right">53.51</td>
    <td align="right">53.15</td>
    <td align="right">59.18</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">62.24</td>
    <td align="right">65.60</td>
    <td align="right">65.21</td>
    <td align="right">70.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.07</td>
    <td align="right">70.96</td>
    <td align="right">70.28</td>
    <td align="right">75.08</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.33</td>
    <td align="right">87.96</td>
    <td align="right">88.91</td>
    <td align="right">93.35</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.96</td>
    <td align="right">97.85</td>
    <td align="right">97.45</td>
    <td align="right">103.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.73</td>
    <td align="right">87.62</td>
    <td align="right">87.32</td>
    <td align="right">90.98</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.02</td>
    <td align="right">107.06</td>
    <td align="right">106.81</td>
    <td align="right">111.74</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.75</td>
    <td align="right">157.92</td>
    <td align="right">157.21</td>
    <td align="right">167.27</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.82</td>
    <td align="right">14.82</td>
    <td align="right">8.36</td>
    <td align="right">17.85</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.53</td>
    <td align="right">29.80</td>
    <td align="right">29.12</td>
    <td align="right">29.55</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.43</td>
    <td align="right">14.60</td>
    <td align="right">14.46</td>
    <td align="right">14.57</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.78</td>
    <td align="right">17.73</td>
    <td align="right">17.73</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.66</td>
    <td align="right">44.50</td>
    <td align="right">31.44</td>
    <td align="right">39.19</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.16</td>
    <td align="right">18.28</td>
    <td align="right">18.24</td>
    <td align="right">18.24</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">21.65</td>
    <td align="right">21.65</td>
    <td align="right">21.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.32</td>
    <td align="right">62.32</td>
    <td align="right">31.52</td>
    <td align="right">51.32</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.58</td>
    <td align="right">21.45</td>
    <td align="right">21.45</td>
    <td align="right">21.47</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.11</td>
    <td align="right">23.00</td>
    <td align="right">23.05</td>
    <td align="right">23.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.54</td>
    <td align="right">77.23</td>
    <td align="right">32.50</td>
    <td align="right">58.15</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.23</td>
    <td align="right">23.40</td>
    <td align="right">23.47</td>
    <td align="right">23.40</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">25.72</td>
    <td align="right">25.78</td>
    <td align="right">25.72</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.52</td>
    <td align="right">30.74</td>
    <td align="right">30.48</td>
    <td align="right">30.65</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">14.48</td>
    <td align="right">14.63</td>
    <td align="right">14.48</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">17.76</td>
    <td align="right">17.80</td>
    <td align="right">17.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.65</td>
    <td align="right">48.24</td>
    <td align="right">48.15</td>
    <td align="right">47.98</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.16</td>
    <td align="right">18.22</td>
    <td align="right">18.21</td>
    <td align="right">18.23</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.22</td>
    <td align="right">21.72</td>
    <td align="right">21.61</td>
    <td align="right">21.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.37</td>
    <td align="right">58.28</td>
    <td align="right">57.72</td>
    <td align="right">57.55</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.60</td>
    <td align="right">21.34</td>
    <td align="right">21.44</td>
    <td align="right">21.37</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.06</td>
    <td align="right">23.23</td>
    <td align="right">23.05</td>
    <td align="right">23.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">58.87</td>
    <td align="right">74.09</td>
    <td align="right">77.68</td>
    <td align="right">74.01</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.24</td>
    <td align="right">23.49</td>
    <td align="right">23.48</td>
    <td align="right">23.39</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.05</td>
    <td align="right">25.76</td>
    <td align="right">25.75</td>
    <td align="right">25.74</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.61</td>
    <td align="right">31.90</td>
    <td align="right">28.32</td>
    <td align="right">30.32</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.47</td>
    <td align="right">14.60</td>
    <td align="right">14.48</td>
    <td align="right">14.49</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.84</td>
    <td align="right">17.77</td>
    <td align="right">17.81</td>
    <td align="right">17.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.90</td>
    <td align="right">48.56</td>
    <td align="right">30.30</td>
    <td align="right">41.49</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.05</td>
    <td align="right">18.24</td>
    <td align="right">18.28</td>
    <td align="right">18.23</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.20</td>
    <td align="right">21.67</td>
    <td align="right">21.75</td>
    <td align="right">21.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.36</td>
    <td align="right">64.69</td>
    <td align="right">34.18</td>
    <td align="right">50.91</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.72</td>
    <td align="right">21.47</td>
    <td align="right">21.36</td>
    <td align="right">21.43</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.05</td>
    <td align="right">22.99</td>
    <td align="right">23.32</td>
    <td align="right">22.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">67.55</td>
    <td align="right">81.60</td>
    <td align="right">34.93</td>
    <td align="right">59.76</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.20</td>
    <td align="right">23.40</td>
    <td align="right">23.54</td>
    <td align="right">23.49</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.08</td>
    <td align="right">25.72</td>
    <td align="right">25.72</td>
    <td align="right">25.72</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.44</td>
    <td align="right">30.35</td>
    <td align="right">30.49</td>
    <td align="right">30.36</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">14.48</td>
    <td align="right">14.60</td>
    <td align="right">14.58</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.86</td>
    <td align="right">17.76</td>
    <td align="right">17.81</td>
    <td align="right">17.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.82</td>
    <td align="right">47.97</td>
    <td align="right">47.99</td>
    <td align="right">47.60</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.04</td>
    <td align="right">18.28</td>
    <td align="right">18.28</td>
    <td align="right">18.24</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.23</td>
    <td align="right">21.77</td>
    <td align="right">21.68</td>
    <td align="right">21.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.37</td>
    <td align="right">57.99</td>
    <td align="right">58.09</td>
    <td align="right">57.74</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.60</td>
    <td align="right">21.47</td>
    <td align="right">21.44</td>
    <td align="right">21.37</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.10</td>
    <td align="right">23.19</td>
    <td align="right">22.99</td>
    <td align="right">23.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">64.63</td>
    <td align="right">69.28</td>
    <td align="right">70.61</td>
    <td align="right">69.57</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">23.53</td>
    <td align="right">23.46</td>
    <td align="right">23.40</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.07</td>
    <td align="right">25.79</td>
    <td align="right">25.74</td>
    <td align="right">25.73</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">20.22</td>
    <td align="right">22.71</td>
    <td align="right">23.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.14</td>
    <td align="right">20.32</td>
    <td align="right">22.41</td>
    <td align="right">23.60</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.98</td>
    <td align="right">9.34</td>
    <td align="right">18.40</td>
    <td align="right">16.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.22</td>
    <td align="right">24.73</td>
    <td align="right">27.44</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.61</td>
    <td align="right">26.25</td>
    <td align="right">24.30</td>
    <td align="right">27.45</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.94</td>
    <td align="right">13.92</td>
    <td align="right">20.66</td>
    <td align="right">20.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.19</td>
    <td align="right">37.95</td>
    <td align="right">26.67</td>
    <td align="right">34.67</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.57</td>
    <td align="right">37.57</td>
    <td align="right">26.34</td>
    <td align="right">34.25</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.87</td>
    <td align="right">16.72</td>
    <td align="right">25.00</td>
    <td align="right">22.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.57</td>
    <td align="right">42.09</td>
    <td align="right">25.89</td>
    <td align="right">38.19</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.44</td>
    <td align="right">44.16</td>
    <td align="right">26.45</td>
    <td align="right">37.81</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.10</td>
    <td align="right">20.18</td>
    <td align="right">21.17</td>
    <td align="right">24.60</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">19.65</td>
    <td align="right">19.66</td>
    <td align="right">19.65</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.08</td>
    <td align="right">20.22</td>
    <td align="right">20.22</td>
    <td align="right">20.23</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.99</td>
    <td align="right">9.89</td>
    <td align="right">9.89</td>
    <td align="right">9.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.70</td>
    <td align="right">28.12</td>
    <td align="right">28.12</td>
    <td align="right">28.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">27.61</td>
    <td align="right">27.62</td>
    <td align="right">27.60</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.94</td>
    <td align="right">15.06</td>
    <td align="right">15.05</td>
    <td align="right">15.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.13</td>
    <td align="right">35.35</td>
    <td align="right">35.28</td>
    <td align="right">35.31</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.58</td>
    <td align="right">34.97</td>
    <td align="right">34.93</td>
    <td align="right">34.86</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.85</td>
    <td align="right">18.18</td>
    <td align="right">18.20</td>
    <td align="right">18.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.73</td>
    <td align="right">38.66</td>
    <td align="right">38.72</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.41</td>
    <td align="right">41.90</td>
    <td align="right">41.94</td>
    <td align="right">41.97</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.12</td>
    <td align="right">20.74</td>
    <td align="right">20.73</td>
    <td align="right">20.75</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">20.46</td>
    <td align="right">23.48</td>
    <td align="right">24.15</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.15</td>
    <td align="right">20.09</td>
    <td align="right">22.91</td>
    <td align="right">24.08</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.56</td>
    <td align="right">9.22</td>
    <td align="right">18.49</td>
    <td align="right">15.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.70</td>
    <td align="right">26.31</td>
    <td align="right">24.54</td>
    <td align="right">28.01</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.16</td>
    <td align="right">25.86</td>
    <td align="right">24.15</td>
    <td align="right">27.39</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.85</td>
    <td align="right">14.26</td>
    <td align="right">20.72</td>
    <td align="right">20.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.97</td>
    <td align="right">38.77</td>
    <td align="right">26.96</td>
    <td align="right">35.13</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">37.21</td>
    <td align="right">26.16</td>
    <td align="right">34.07</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.79</td>
    <td align="right">16.45</td>
    <td align="right">21.85</td>
    <td align="right">22.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.63</td>
    <td align="right">41.82</td>
    <td align="right">26.18</td>
    <td align="right">36.94</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.47</td>
    <td align="right">43.98</td>
    <td align="right">26.71</td>
    <td align="right">37.80</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.06</td>
    <td align="right">20.20</td>
    <td align="right">20.88</td>
    <td align="right">24.90</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">19.66</td>
    <td align="right">19.62</td>
    <td align="right">19.62</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.18</td>
    <td align="right">20.19</td>
    <td align="right">20.20</td>
    <td align="right">20.23</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.58</td>
    <td align="right">9.89</td>
    <td align="right">9.89</td>
    <td align="right">9.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">28.13</td>
    <td align="right">28.12</td>
    <td align="right">28.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">24.95</td>
    <td align="right">27.29</td>
    <td align="right">27.30</td>
    <td align="right">27.27</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.94</td>
    <td align="right">15.05</td>
    <td align="right">15.05</td>
    <td align="right">15.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.98</td>
    <td align="right">35.28</td>
    <td align="right">35.28</td>
    <td align="right">35.32</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.52</td>
    <td align="right">35.01</td>
    <td align="right">34.83</td>
    <td align="right">34.87</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.89</td>
    <td align="right">17.87</td>
    <td align="right">17.86</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.64</td>
    <td align="right">38.52</td>
    <td align="right">38.47</td>
    <td align="right">38.50</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.33</td>
    <td align="right">41.85</td>
    <td align="right">41.87</td>
    <td align="right">42.20</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.04</td>
    <td align="right">20.85</td>
    <td align="right">20.86</td>
    <td align="right">20.85</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.68</td>
    <td align="right">9.09</td>
    <td align="right">17.79</td>
    <td align="right">15.68</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">20.21</td>
    <td align="right">22.71</td>
    <td align="right">23.75</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.06</td>
    <td align="right">20.29</td>
    <td align="right">22.36</td>
    <td align="right">23.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.77</td>
    <td align="right">14.29</td>
    <td align="right">20.34</td>
    <td align="right">19.74</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">26.23</td>
    <td align="right">24.73</td>
    <td align="right">27.45</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">26.19</td>
    <td align="right">24.33</td>
    <td align="right">27.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.31</td>
    <td align="right">15.43</td>
    <td align="right">20.35</td>
    <td align="right">20.79</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.17</td>
    <td align="right">38.09</td>
    <td align="right">26.64</td>
    <td align="right">34.67</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.57</td>
    <td align="right">37.50</td>
    <td align="right">26.33</td>
    <td align="right">34.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.81</td>
    <td align="right">19.91</td>
    <td align="right">20.66</td>
    <td align="right">24.80</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.50</td>
    <td align="right">41.87</td>
    <td align="right">25.94</td>
    <td align="right">36.78</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.45</td>
    <td align="right">44.16</td>
    <td align="right">26.45</td>
    <td align="right">37.73</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.50</td>
    <td align="right">9.70</td>
    <td align="right">9.74</td>
    <td align="right">9.70</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.06</td>
    <td align="right">19.66</td>
    <td align="right">19.93</td>
    <td align="right">19.69</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.13</td>
    <td align="right">20.20</td>
    <td align="right">20.20</td>
    <td align="right">20.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.90</td>
    <td align="right">14.82</td>
    <td align="right">14.83</td>
    <td align="right">14.83</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">28.12</td>
    <td align="right">28.11</td>
    <td align="right">28.11</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">27.60</td>
    <td align="right">27.60</td>
    <td align="right">27.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">17.52</td>
    <td align="right">17.53</td>
    <td align="right">17.54</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.19</td>
    <td align="right">35.37</td>
    <td align="right">35.41</td>
    <td align="right">35.39</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">35.27</td>
    <td align="right">34.83</td>
    <td align="right">35.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">20.72</td>
    <td align="right">20.75</td>
    <td align="right">20.76</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.54</td>
    <td align="right">38.66</td>
    <td align="right">38.70</td>
    <td align="right">38.74</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.43</td>
    <td align="right">41.86</td>
    <td align="right">42.03</td>
    <td align="right">42.01</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.09</td>
    <td align="right">9.07</td>
    <td align="right">17.30</td>
    <td align="right">15.44</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">20.49</td>
    <td align="right">23.52</td>
    <td align="right">24.13</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.18</td>
    <td align="right">20.34</td>
    <td align="right">22.88</td>
    <td align="right">24.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.92</td>
    <td align="right">14.35</td>
    <td align="right">20.71</td>
    <td align="right">20.11</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.68</td>
    <td align="right">24.57</td>
    <td align="right">27.95</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.12</td>
    <td align="right">26.06</td>
    <td align="right">24.13</td>
    <td align="right">27.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">15.22</td>
    <td align="right">20.52</td>
    <td align="right">20.89</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.95</td>
    <td align="right">38.86</td>
    <td align="right">26.94</td>
    <td align="right">34.97</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.56</td>
    <td align="right">37.17</td>
    <td align="right">26.16</td>
    <td align="right">34.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">19.85</td>
    <td align="right">20.75</td>
    <td align="right">24.56</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.59</td>
    <td align="right">41.75</td>
    <td align="right">26.16</td>
    <td align="right">36.79</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.37</td>
    <td align="right">44.02</td>
    <td align="right">26.70</td>
    <td align="right">37.85</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.10</td>
    <td align="right">9.89</td>
    <td align="right">9.74</td>
    <td align="right">9.72</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">19.64</td>
    <td align="right">19.93</td>
    <td align="right">19.93</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.18</td>
    <td align="right">20.18</td>
    <td align="right">20.17</td>
    <td align="right">20.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.90</td>
    <td align="right">14.83</td>
    <td align="right">14.83</td>
    <td align="right">14.86</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">28.12</td>
    <td align="right">28.12</td>
    <td align="right">28.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.19</td>
    <td align="right">27.59</td>
    <td align="right">27.61</td>
    <td align="right">27.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">17.55</td>
    <td align="right">17.54</td>
    <td align="right">17.55</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.96</td>
    <td align="right">35.29</td>
    <td align="right">35.24</td>
    <td align="right">35.25</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.49</td>
    <td align="right">34.84</td>
    <td align="right">34.86</td>
    <td align="right">34.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.84</td>
    <td align="right">20.74</td>
    <td align="right">20.72</td>
    <td align="right">20.72</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">38.50</td>
    <td align="right">38.44</td>
    <td align="right">38.46</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.42</td>
    <td align="right">41.91</td>
    <td align="right">41.91</td>
    <td align="right">42.02</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.24</td>
    <td align="right">21.05</td>
    <td align="right">23.81</td>
    <td align="right">24.38</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.34</td>
    <td align="right">43.22</td>
    <td align="right">40.61</td>
    <td align="right">41.11</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.00</td>
    <td align="right">29.94</td>
    <td align="right">29.20</td>
    <td align="right">29.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.01</td>
    <td align="right">29.77</td>
    <td align="right">24.28</td>
    <td align="right">30.44</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.57</td>
    <td align="right">47.06</td>
    <td align="right">39.42</td>
    <td align="right">44.92</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.71</td>
    <td align="right">39.07</td>
    <td align="right">30.22</td>
    <td align="right">35.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.14</td>
    <td align="right">36.02</td>
    <td align="right">24.59</td>
    <td align="right">33.81</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.39</td>
    <td align="right">54.94</td>
    <td align="right">40.36</td>
    <td align="right">47.73</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.69</td>
    <td align="right">45.73</td>
    <td align="right">32.05</td>
    <td align="right">40.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.75</td>
    <td align="right">47.73</td>
    <td align="right">30.22</td>
    <td align="right">41.74</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.62</td>
    <td align="right">59.45</td>
    <td align="right">45.17</td>
    <td align="right">53.17</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.20</td>
    <td align="right">58.05</td>
    <td align="right">33.55</td>
    <td align="right">47.16</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.26</td>
    <td align="right">20.93</td>
    <td align="right">20.93</td>
    <td align="right">20.94</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.59</td>
    <td align="right">38.94</td>
    <td align="right">38.98</td>
    <td align="right">39.09</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.83</td>
    <td align="right">27.69</td>
    <td align="right">27.69</td>
    <td align="right">27.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.00</td>
    <td align="right">27.88</td>
    <td align="right">27.89</td>
    <td align="right">27.88</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.57</td>
    <td align="right">44.53</td>
    <td align="right">44.47</td>
    <td align="right">44.55</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.59</td>
    <td align="right">36.14</td>
    <td align="right">36.14</td>
    <td align="right">36.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.11</td>
    <td align="right">32.95</td>
    <td align="right">32.94</td>
    <td align="right">32.95</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.89</td>
    <td align="right">49.36</td>
    <td align="right">49.89</td>
    <td align="right">49.38</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.77</td>
    <td align="right">38.75</td>
    <td align="right">38.55</td>
    <td align="right">38.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.76</td>
    <td align="right">38.84</td>
    <td align="right">38.83</td>
    <td align="right">38.86</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.00</td>
    <td align="right">53.47</td>
    <td align="right">53.38</td>
    <td align="right">53.50</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.26</td>
    <td align="right">51.18</td>
    <td align="right">51.20</td>
    <td align="right">50.64</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.24</td>
    <td align="right">21.04</td>
    <td align="right">23.82</td>
    <td align="right">24.38</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.49</td>
    <td align="right">42.78</td>
    <td align="right">41.47</td>
    <td align="right">42.08</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.95</td>
    <td align="right">29.81</td>
    <td align="right">29.50</td>
    <td align="right">29.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.01</td>
    <td align="right">29.76</td>
    <td align="right">24.22</td>
    <td align="right">30.05</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.19</td>
    <td align="right">46.43</td>
    <td align="right">39.48</td>
    <td align="right">43.55</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.85</td>
    <td align="right">39.52</td>
    <td align="right">30.12</td>
    <td align="right">35.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.12</td>
    <td align="right">35.91</td>
    <td align="right">24.62</td>
    <td align="right">33.99</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.63</td>
    <td align="right">57.73</td>
    <td align="right">40.85</td>
    <td align="right">48.96</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.63</td>
    <td align="right">45.69</td>
    <td align="right">32.87</td>
    <td align="right">40.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.73</td>
    <td align="right">47.73</td>
    <td align="right">30.36</td>
    <td align="right">41.75</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.28</td>
    <td align="right">59.60</td>
    <td align="right">44.65</td>
    <td align="right">52.84</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.42</td>
    <td align="right">57.97</td>
    <td align="right">33.28</td>
    <td align="right">47.28</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.26</td>
    <td align="right">21.14</td>
    <td align="right">20.94</td>
    <td align="right">20.95</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.55</td>
    <td align="right">38.69</td>
    <td align="right">38.93</td>
    <td align="right">38.68</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.87</td>
    <td align="right">27.91</td>
    <td align="right">27.93</td>
    <td align="right">27.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.02</td>
    <td align="right">27.90</td>
    <td align="right">27.89</td>
    <td align="right">27.89</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.13</td>
    <td align="right">43.46</td>
    <td align="right">43.21</td>
    <td align="right">43.58</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.89</td>
    <td align="right">37.04</td>
    <td align="right">36.97</td>
    <td align="right">36.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.15</td>
    <td align="right">32.96</td>
    <td align="right">32.97</td>
    <td align="right">32.96</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">61.38</td>
    <td align="right">49.33</td>
    <td align="right">49.35</td>
    <td align="right">49.11</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.68</td>
    <td align="right">38.59</td>
    <td align="right">38.60</td>
    <td align="right">38.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.76</td>
    <td align="right">38.86</td>
    <td align="right">38.89</td>
    <td align="right">38.85</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.87</td>
    <td align="right">52.96</td>
    <td align="right">53.10</td>
    <td align="right">52.87</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.23</td>
    <td align="right">51.58</td>
    <td align="right">51.82</td>
    <td align="right">51.52</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">123.70</td>
    <td align="right">61.78</td>
    <td align="right">22.64</td>
    <td align="right">53.06</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">27.56</td>
    <td align="right">37.13</td>
    <td align="right">34.41</td>
    <td align="right">36.47</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.17</td>
    <td align="right">16.13</td>
    <td align="right">16.16</td>
    <td align="right">16.13</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.64</td>
    <td align="right">20.54</td>
    <td align="right">20.59</td>
    <td align="right">20.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">77.68</td>
    <td align="right">98.88</td>
    <td align="right">46.87</td>
    <td align="right">74.26</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">27.77</td>
    <td align="right">29.98</td>
    <td align="right">30.00</td>
    <td align="right">30.00</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.17</td>
    <td align="right">33.21</td>
    <td align="right">33.01</td>
    <td align="right">33.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.34</td>
    <td align="right">196.94</td>
    <td align="right">63.78</td>
    <td align="right">132.31</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.21</td>
    <td align="right">48.10</td>
    <td align="right">48.02</td>
    <td align="right">48.08</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.27</td>
    <td align="right">51.99</td>
    <td align="right">51.70</td>
    <td align="right">51.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">248.90</td>
    <td align="right">301.84</td>
    <td align="right">78.60</td>
    <td align="right">188.96</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.60</td>
    <td align="right">65.09</td>
    <td align="right">65.03</td>
    <td align="right">64.86</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">68.03</td>
    <td align="right">69.25</td>
    <td align="right">69.42</td>
    <td align="right">69.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">28.62</td>
    <td align="right">39.57</td>
    <td align="right">39.75</td>
    <td align="right">39.52</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.39</td>
    <td align="right">17.42</td>
    <td align="right">17.46</td>
    <td align="right">17.38</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.01</td>
    <td align="right">20.86</td>
    <td align="right">20.95</td>
    <td align="right">20.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">76.77</td>
    <td align="right">102.92</td>
    <td align="right">102.74</td>
    <td align="right">102.52</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.81</td>
    <td align="right">28.73</td>
    <td align="right">28.72</td>
    <td align="right">28.71</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.45</td>
    <td align="right">31.63</td>
    <td align="right">31.52</td>
    <td align="right">31.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">143.15</td>
    <td align="right">191.26</td>
    <td align="right">191.37</td>
    <td align="right">190.56</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.87</td>
    <td align="right">47.69</td>
    <td align="right">47.77</td>
    <td align="right">47.67</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.66</td>
    <td align="right">52.17</td>
    <td align="right">52.18</td>
    <td align="right">52.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">248.58</td>
    <td align="right">298.05</td>
    <td align="right">298.22</td>
    <td align="right">298.01</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">63.84</td>
    <td align="right">64.68</td>
    <td align="right">64.81</td>
    <td align="right">64.70</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.46</td>
    <td align="right">68.70</td>
    <td align="right">68.75</td>
    <td align="right">68.74</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.87</td>
    <td align="right">39.03</td>
    <td align="right">32.89</td>
    <td align="right">37.21</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">13.61</td>
    <td align="right">15.60</td>
    <td align="right">15.56</td>
    <td align="right">15.58</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.59</td>
    <td align="right">21.50</td>
    <td align="right">21.59</td>
    <td align="right">21.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">70.98</td>
    <td align="right">101.93</td>
    <td align="right">43.78</td>
    <td align="right">75.37</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.49</td>
    <td align="right">28.03</td>
    <td align="right">27.75</td>
    <td align="right">27.77</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.08</td>
    <td align="right">35.95</td>
    <td align="right">35.94</td>
    <td align="right">35.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.61</td>
    <td align="right">206.01</td>
    <td align="right">71.90</td>
    <td align="right">149.86</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.22</td>
    <td align="right">49.40</td>
    <td align="right">49.47</td>
    <td align="right">49.42</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.91</td>
    <td align="right">51.21</td>
    <td align="right">51.00</td>
    <td align="right">51.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">270.62</td>
    <td align="right">332.13</td>
    <td align="right">84.76</td>
    <td align="right">208.26</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.19</td>
    <td align="right">64.64</td>
    <td align="right">64.70</td>
    <td align="right">64.76</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.75</td>
    <td align="right">69.03</td>
    <td align="right">69.04</td>
    <td align="right">69.12</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">25.67</td>
    <td align="right">35.50</td>
    <td align="right">35.54</td>
    <td align="right">35.39</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.85</td>
    <td align="right">17.05</td>
    <td align="right">16.82</td>
    <td align="right">16.91</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.22</td>
    <td align="right">19.15</td>
    <td align="right">19.21</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">77.77</td>
    <td align="right">102.92</td>
    <td align="right">102.63</td>
    <td align="right">105.86</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.25</td>
    <td align="right">28.38</td>
    <td align="right">28.35</td>
    <td align="right">28.38</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.76</td>
    <td align="right">35.32</td>
    <td align="right">35.35</td>
    <td align="right">35.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.55</td>
    <td align="right">193.06</td>
    <td align="right">191.12</td>
    <td align="right">208.44</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.11</td>
    <td align="right">49.02</td>
    <td align="right">49.21</td>
    <td align="right">49.27</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.98</td>
    <td align="right">51.14</td>
    <td align="right">51.02</td>
    <td align="right">51.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">268.89</td>
    <td align="right">295.43</td>
    <td align="right">295.90</td>
    <td align="right">290.03</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.02</td>
    <td align="right">62.84</td>
    <td align="right">67.34</td>
    <td align="right">67.99</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.74</td>
    <td align="right">67.46</td>
    <td align="right">67.45</td>
    <td align="right">67.44</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.20</td>
    <td align="right">24.23</td>
    <td align="right">25.27</td>
    <td align="right">29.25</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.95</td>
    <td align="right">24.03</td>
    <td align="right">24.75</td>
    <td align="right">28.65</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.96</td>
    <td align="right">11.32</td>
    <td align="right">20.17</td>
    <td align="right">18.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.39</td>
    <td align="right">39.88</td>
    <td align="right">32.89</td>
    <td align="right">41.40</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.25</td>
    <td align="right">42.39</td>
    <td align="right">32.83</td>
    <td align="right">42.80</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">20.97</td>
    <td align="right">23.25</td>
    <td align="right">26.80</td>
    <td align="right">28.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.02</td>
    <td align="right">69.92</td>
    <td align="right">42.35</td>
    <td align="right">63.65</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.94</td>
    <td align="right">70.24</td>
    <td align="right">42.96</td>
    <td align="right">64.26</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.66</td>
    <td align="right">40.06</td>
    <td align="right">42.14</td>
    <td align="right">41.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.00</td>
    <td align="right">90.12</td>
    <td align="right">47.09</td>
    <td align="right">80.14</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.51</td>
    <td align="right">96.26</td>
    <td align="right">50.26</td>
    <td align="right">85.31</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.92</td>
    <td align="right">52.81</td>
    <td align="right">38.12</td>
    <td align="right">52.85</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.11</td>
    <td align="right">24.21</td>
    <td align="right">24.28</td>
    <td align="right">24.34</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.58</td>
    <td align="right">25.46</td>
    <td align="right">25.41</td>
    <td align="right">25.41</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">8.81</td>
    <td align="right">10.88</td>
    <td align="right">10.84</td>
    <td align="right">10.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.02</td>
    <td align="right">42.09</td>
    <td align="right">42.13</td>
    <td align="right">42.09</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">47.18</td>
    <td align="right">48.32</td>
    <td align="right">48.46</td>
    <td align="right">48.35</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.52</td>
    <td align="right">24.42</td>
    <td align="right">24.51</td>
    <td align="right">24.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">65.84</td>
    <td align="right">67.91</td>
    <td align="right">67.89</td>
    <td align="right">67.83</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.40</td>
    <td align="right">67.74</td>
    <td align="right">67.95</td>
    <td align="right">67.79</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.54</td>
    <td align="right">41.59</td>
    <td align="right">41.62</td>
    <td align="right">41.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.99</td>
    <td align="right">89.17</td>
    <td align="right">89.06</td>
    <td align="right">89.03</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.89</td>
    <td align="right">92.55</td>
    <td align="right">92.65</td>
    <td align="right">92.56</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.15</td>
    <td align="right">53.26</td>
    <td align="right">53.02</td>
    <td align="right">52.94</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.31</td>
    <td align="right">24.39</td>
    <td align="right">26.07</td>
    <td align="right">29.34</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.08</td>
    <td align="right">24.18</td>
    <td align="right">25.41</td>
    <td align="right">29.39</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.29</td>
    <td align="right">11.02</td>
    <td align="right">19.97</td>
    <td align="right">18.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.90</td>
    <td align="right">38.07</td>
    <td align="right">31.49</td>
    <td align="right">40.05</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.30</td>
    <td align="right">43.32</td>
    <td align="right">33.22</td>
    <td align="right">43.57</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.31</td>
    <td align="right">21.69</td>
    <td align="right">25.71</td>
    <td align="right">27.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.26</td>
    <td align="right">70.19</td>
    <td align="right">42.21</td>
    <td align="right">63.21</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.33</td>
    <td align="right">73.15</td>
    <td align="right">43.98</td>
    <td align="right">66.89</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.83</td>
    <td align="right">40.60</td>
    <td align="right">35.12</td>
    <td align="right">41.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.01</td>
    <td align="right">90.53</td>
    <td align="right">47.49</td>
    <td align="right">80.47</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.08</td>
    <td align="right">95.34</td>
    <td align="right">50.65</td>
    <td align="right">84.42</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.06</td>
    <td align="right">53.09</td>
    <td align="right">37.52</td>
    <td align="right">52.96</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.38</td>
    <td align="right">23.32</td>
    <td align="right">23.61</td>
    <td align="right">23.32</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.07</td>
    <td align="right">24.75</td>
    <td align="right">24.77</td>
    <td align="right">24.73</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.27</td>
    <td align="right">11.85</td>
    <td align="right">12.23</td>
    <td align="right">11.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.21</td>
    <td align="right">42.10</td>
    <td align="right">42.07</td>
    <td align="right">42.14</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.04</td>
    <td align="right">42.18</td>
    <td align="right">42.13</td>
    <td align="right">42.08</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">20.98</td>
    <td align="right">22.04</td>
    <td align="right">22.04</td>
    <td align="right">21.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.66</td>
    <td align="right">68.53</td>
    <td align="right">68.48</td>
    <td align="right">68.52</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.30</td>
    <td align="right">69.46</td>
    <td align="right">69.45</td>
    <td align="right">69.21</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.95</td>
    <td align="right">41.35</td>
    <td align="right">41.41</td>
    <td align="right">41.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.63</td>
    <td align="right">87.63</td>
    <td align="right">87.55</td>
    <td align="right">87.51</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.40</td>
    <td align="right">92.54</td>
    <td align="right">92.44</td>
    <td align="right">92.41</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.00</td>
    <td align="right">52.85</td>
    <td align="right">52.73</td>
    <td align="right">52.86</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.83</td>
    <td align="right">11.77</td>
    <td align="right">19.76</td>
    <td align="right">18.44</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.04</td>
    <td align="right">22.96</td>
    <td align="right">24.56</td>
    <td align="right">28.00</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.52</td>
    <td align="right">24.92</td>
    <td align="right">25.24</td>
    <td align="right">29.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">21.22</td>
    <td align="right">24.37</td>
    <td align="right">26.42</td>
    <td align="right">28.19</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.36</td>
    <td align="right">38.95</td>
    <td align="right">32.54</td>
    <td align="right">40.85</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.93</td>
    <td align="right">44.42</td>
    <td align="right">33.87</td>
    <td align="right">44.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.34</td>
    <td align="right">38.68</td>
    <td align="right">33.19</td>
    <td align="right">39.71</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.89</td>
    <td align="right">72.83</td>
    <td align="right">43.52</td>
    <td align="right">66.14</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.62</td>
    <td align="right">72.21</td>
    <td align="right">43.92</td>
    <td align="right">66.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.31</td>
    <td align="right">53.76</td>
    <td align="right">38.25</td>
    <td align="right">54.11</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.61</td>
    <td align="right">92.23</td>
    <td align="right">47.94</td>
    <td align="right">82.11</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.25</td>
    <td align="right">91.69</td>
    <td align="right">48.68</td>
    <td align="right">80.71</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">10.52</td>
    <td align="right">12.75</td>
    <td align="right">12.79</td>
    <td align="right">12.68</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">18.89</td>
    <td align="right">22.99</td>
    <td align="right">23.28</td>
    <td align="right">23.02</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.65</td>
    <td align="right">25.50</td>
    <td align="right">25.51</td>
    <td align="right">25.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">21.94</td>
    <td align="right">23.40</td>
    <td align="right">23.39</td>
    <td align="right">23.00</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.63</td>
    <td align="right">42.79</td>
    <td align="right">42.78</td>
    <td align="right">42.86</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.68</td>
    <td align="right">45.05</td>
    <td align="right">45.27</td>
    <td align="right">45.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.17</td>
    <td align="right">41.55</td>
    <td align="right">41.58</td>
    <td align="right">42.72</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.04</td>
    <td align="right">67.72</td>
    <td align="right">67.75</td>
    <td align="right">67.86</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.63</td>
    <td align="right">71.06</td>
    <td align="right">70.74</td>
    <td align="right">70.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.04</td>
    <td align="right">53.34</td>
    <td align="right">53.30</td>
    <td align="right">53.47</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.32</td>
    <td align="right">89.09</td>
    <td align="right">89.04</td>
    <td align="right">89.02</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.19</td>
    <td align="right">95.33</td>
    <td align="right">95.44</td>
    <td align="right">95.38</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.74</td>
    <td align="right">11.84</td>
    <td align="right">19.54</td>
    <td align="right">18.20</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.19</td>
    <td align="right">23.17</td>
    <td align="right">25.43</td>
    <td align="right">28.18</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.62</td>
    <td align="right">22.50</td>
    <td align="right">24.40</td>
    <td align="right">27.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.41</td>
    <td align="right">24.96</td>
    <td align="right">27.05</td>
    <td align="right">28.85</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.44</td>
    <td align="right">37.67</td>
    <td align="right">31.64</td>
    <td align="right">40.04</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.31</td>
    <td align="right">42.46</td>
    <td align="right">32.79</td>
    <td align="right">42.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.92</td>
    <td align="right">37.83</td>
    <td align="right">32.81</td>
    <td align="right">39.25</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.52</td>
    <td align="right">73.21</td>
    <td align="right">43.34</td>
    <td align="right">66.05</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.57</td>
    <td align="right">70.69</td>
    <td align="right">43.08</td>
    <td align="right">64.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.34</td>
    <td align="right">53.59</td>
    <td align="right">38.07</td>
    <td align="right">53.77</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.28</td>
    <td align="right">91.28</td>
    <td align="right">47.67</td>
    <td align="right">81.09</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.21</td>
    <td align="right">93.75</td>
    <td align="right">49.99</td>
    <td align="right">82.93</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.67</td>
    <td align="right">12.57</td>
    <td align="right">12.69</td>
    <td align="right">12.37</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.38</td>
    <td align="right">23.66</td>
    <td align="right">23.76</td>
    <td align="right">23.61</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.86</td>
    <td align="right">25.51</td>
    <td align="right">25.55</td>
    <td align="right">25.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">21.79</td>
    <td align="right">22.79</td>
    <td align="right">22.90</td>
    <td align="right">22.88</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">37.65</td>
    <td align="right">45.44</td>
    <td align="right">45.37</td>
    <td align="right">45.41</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.71</td>
    <td align="right">45.50</td>
    <td align="right">45.45</td>
    <td align="right">45.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.70</td>
    <td align="right">41.25</td>
    <td align="right">41.22</td>
    <td align="right">41.09</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.18</td>
    <td align="right">68.22</td>
    <td align="right">68.32</td>
    <td align="right">68.19</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.69</td>
    <td align="right">68.43</td>
    <td align="right">68.29</td>
    <td align="right">68.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">52.93</td>
    <td align="right">53.12</td>
    <td align="right">53.19</td>
    <td align="right">53.17</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.19</td>
    <td align="right">86.78</td>
    <td align="right">86.87</td>
    <td align="right">86.79</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.98</td>
    <td align="right">93.73</td>
    <td align="right">93.75</td>
    <td align="right">93.81</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.11</td>
    <td align="right">24.63</td>
    <td align="right">25.95</td>
    <td align="right">29.18</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">51.00</td>
    <td align="right">45.69</td>
    <td align="right">43.62</td>
    <td align="right">44.18</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">30.99</td>
    <td align="right">34.12</td>
    <td align="right">31.79</td>
    <td align="right">34.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.82</td>
    <td align="right">39.26</td>
    <td align="right">29.83</td>
    <td align="right">39.48</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.28</td>
    <td align="right">58.37</td>
    <td align="right">48.59</td>
    <td align="right">55.16</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.36</td>
    <td align="right">58.84</td>
    <td align="right">38.41</td>
    <td align="right">52.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.05</td>
    <td align="right">64.78</td>
    <td align="right">41.11</td>
    <td align="right">62.61</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.72</td>
    <td align="right">87.90</td>
    <td align="right">63.33</td>
    <td align="right">79.33</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.13</td>
    <td align="right">89.22</td>
    <td align="right">43.81</td>
    <td align="right">74.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.80</td>
    <td align="right">88.51</td>
    <td align="right">56.63</td>
    <td align="right">81.85</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.97</td>
    <td align="right">107.27</td>
    <td align="right">80.43</td>
    <td align="right">97.67</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.97</td>
    <td align="right">134.02</td>
    <td align="right">51.21</td>
    <td align="right">105.98</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.19</td>
    <td align="right">25.12</td>
    <td align="right">25.10</td>
    <td align="right">25.09</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.36</td>
    <td align="right">40.47</td>
    <td align="right">40.46</td>
    <td align="right">40.52</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.71</td>
    <td align="right">34.97</td>
    <td align="right">33.91</td>
    <td align="right">33.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.76</td>
    <td align="right">40.68</td>
    <td align="right">40.62</td>
    <td align="right">40.61</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">66.80</td>
    <td align="right">56.68</td>
    <td align="right">56.63</td>
    <td align="right">56.50</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.94</td>
    <td align="right">56.31</td>
    <td align="right">56.28</td>
    <td align="right">56.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.38</td>
    <td align="right">59.98</td>
    <td align="right">59.96</td>
    <td align="right">60.06</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.34</td>
    <td align="right">81.88</td>
    <td align="right">82.10</td>
    <td align="right">81.78</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.09</td>
    <td align="right">80.55</td>
    <td align="right">80.58</td>
    <td align="right">80.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.60</td>
    <td align="right">80.55</td>
    <td align="right">80.57</td>
    <td align="right">80.61</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">110.75</td>
    <td align="right">98.75</td>
    <td align="right">98.77</td>
    <td align="right">98.93</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">130.67</td>
    <td align="right">118.44</td>
    <td align="right">118.50</td>
    <td align="right">118.50</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.48</td>
    <td align="right">24.75</td>
    <td align="right">26.44</td>
    <td align="right">29.51</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">51.41</td>
    <td align="right">45.56</td>
    <td align="right">44.47</td>
    <td align="right">45.22</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.55</td>
    <td align="right">36.84</td>
    <td align="right">33.47</td>
    <td align="right">37.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.75</td>
    <td align="right">42.79</td>
    <td align="right">31.03</td>
    <td align="right">42.95</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.28</td>
    <td align="right">59.63</td>
    <td align="right">51.20</td>
    <td align="right">56.69</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">60.16</td>
    <td align="right">61.72</td>
    <td align="right">38.84</td>
    <td align="right">54.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.81</td>
    <td align="right">62.99</td>
    <td align="right">40.39</td>
    <td align="right">60.93</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.33</td>
    <td align="right">88.97</td>
    <td align="right">62.88</td>
    <td align="right">80.76</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.17</td>
    <td align="right">88.64</td>
    <td align="right">42.55</td>
    <td align="right">74.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.13</td>
    <td align="right">88.93</td>
    <td align="right">56.98</td>
    <td align="right">82.38</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">110.15</td>
    <td align="right">106.08</td>
    <td align="right">78.81</td>
    <td align="right">96.19</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.90</td>
    <td align="right">133.67</td>
    <td align="right">49.91</td>
    <td align="right">104.58</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.37</td>
    <td align="right">25.30</td>
    <td align="right">25.50</td>
    <td align="right">25.39</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.30</td>
    <td align="right">40.16</td>
    <td align="right">40.39</td>
    <td align="right">40.08</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.55</td>
    <td align="right">34.98</td>
    <td align="right">34.91</td>
    <td align="right">34.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.18</td>
    <td align="right">42.54</td>
    <td align="right">42.36</td>
    <td align="right">42.41</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">65.51</td>
    <td align="right">57.97</td>
    <td align="right">57.90</td>
    <td align="right">57.88</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.15</td>
    <td align="right">57.87</td>
    <td align="right">57.83</td>
    <td align="right">57.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.93</td>
    <td align="right">60.43</td>
    <td align="right">60.33</td>
    <td align="right">60.17</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.84</td>
    <td align="right">81.19</td>
    <td align="right">82.92</td>
    <td align="right">81.03</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.20</td>
    <td align="right">81.32</td>
    <td align="right">81.44</td>
    <td align="right">81.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.76</td>
    <td align="right">79.22</td>
    <td align="right">79.13</td>
    <td align="right">79.26</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.79</td>
    <td align="right">98.86</td>
    <td align="right">99.00</td>
    <td align="right">98.96</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">133.11</td>
    <td align="right">120.18</td>
    <td align="right">120.42</td>
    <td align="right">120.49</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.88</td>
    <td align="right">7.10</td>
    <td align="right">5.37</td>
    <td align="right">12.21</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">67.24</td>
    <td align="right">59.22</td>
    <td align="right">40.11</td>
    <td align="right">49.77</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.88</td>
    <td align="right">21.06</td>
    <td align="right">23.93</td>
    <td align="right">25.71</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.98</td>
    <td align="right">25.64</td>
    <td align="right">26.50</td>
    <td align="right">29.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">98.95</td>
    <td align="right">86.01</td>
    <td align="right">41.02</td>
    <td align="right">63.77</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.48</td>
    <td align="right">23.66</td>
    <td align="right">24.42</td>
    <td align="right">27.44</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.59</td>
    <td align="right">28.47</td>
    <td align="right">28.82</td>
    <td align="right">30.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">126.95</td>
    <td align="right">103.91</td>
    <td align="right">40.47</td>
    <td align="right">72.14</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">26.65</td>
    <td align="right">26.16</td>
    <td align="right">26.24</td>
    <td align="right">29.82</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">31.10</td>
    <td align="right">31.27</td>
    <td align="right">30.35</td>
    <td align="right">32.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">166.77</td>
    <td align="right">135.42</td>
    <td align="right">41.07</td>
    <td align="right">87.80</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.75</td>
    <td align="right">27.09</td>
    <td align="right">27.97</td>
    <td align="right">31.09</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.60</td>
    <td align="right">32.34</td>
    <td align="right">33.08</td>
    <td align="right">36.18</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">68.25</td>
    <td align="right">62.27</td>
    <td align="right">61.79</td>
    <td align="right">66.60</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.99</td>
    <td align="right">21.14</td>
    <td align="right">23.95</td>
    <td align="right">25.86</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.02</td>
    <td align="right">25.76</td>
    <td align="right">27.00</td>
    <td align="right">28.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">104.13</td>
    <td align="right">91.22</td>
    <td align="right">91.46</td>
    <td align="right">95.53</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.47</td>
    <td align="right">23.73</td>
    <td align="right">24.41</td>
    <td align="right">27.78</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.65</td>
    <td align="right">28.59</td>
    <td align="right">28.99</td>
    <td align="right">30.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.08</td>
    <td align="right">108.76</td>
    <td align="right">108.88</td>
    <td align="right">114.57</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.47</td>
    <td align="right">26.26</td>
    <td align="right">26.21</td>
    <td align="right">29.43</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.16</td>
    <td align="right">31.27</td>
    <td align="right">30.35</td>
    <td align="right">33.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">162.73</td>
    <td align="right">140.49</td>
    <td align="right">140.47</td>
    <td align="right">144.62</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.64</td>
    <td align="right">27.09</td>
    <td align="right">27.96</td>
    <td align="right">30.89</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">33.13</td>
    <td align="right">32.14</td>
    <td align="right">32.98</td>
    <td align="right">35.39</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.65</td>
    <td align="right">60.57</td>
    <td align="right">41.72</td>
    <td align="right">51.21</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.01</td>
    <td align="right">21.52</td>
    <td align="right">24.30</td>
    <td align="right">26.51</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.03</td>
    <td align="right">24.79</td>
    <td align="right">26.33</td>
    <td align="right">28.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">103.61</td>
    <td align="right">96.09</td>
    <td align="right">46.52</td>
    <td align="right">70.68</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.90</td>
    <td align="right">23.14</td>
    <td align="right">25.07</td>
    <td align="right">28.72</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.76</td>
    <td align="right">27.60</td>
    <td align="right">28.15</td>
    <td align="right">30.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">123.09</td>
    <td align="right">115.14</td>
    <td align="right">45.34</td>
    <td align="right">79.22</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">26.77</td>
    <td align="right">25.69</td>
    <td align="right">26.39</td>
    <td align="right">31.63</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.49</td>
    <td align="right">29.97</td>
    <td align="right">29.59</td>
    <td align="right">32.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">164.68</td>
    <td align="right">152.22</td>
    <td align="right">45.26</td>
    <td align="right">97.73</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.92</td>
    <td align="right">27.10</td>
    <td align="right">27.63</td>
    <td align="right">33.32</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.60</td>
    <td align="right">31.80</td>
    <td align="right">31.75</td>
    <td align="right">35.27</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.58</td>
    <td align="right">66.72</td>
    <td align="right">66.68</td>
    <td align="right">71.20</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.12</td>
    <td align="right">21.73</td>
    <td align="right">24.72</td>
    <td align="right">26.63</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.02</td>
    <td align="right">25.17</td>
    <td align="right">26.81</td>
    <td align="right">28.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">98.98</td>
    <td align="right">97.97</td>
    <td align="right">98.33</td>
    <td align="right">105.22</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.96</td>
    <td align="right">23.14</td>
    <td align="right">24.96</td>
    <td align="right">28.65</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.82</td>
    <td align="right">27.65</td>
    <td align="right">28.42</td>
    <td align="right">30.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.25</td>
    <td align="right">122.18</td>
    <td align="right">122.86</td>
    <td align="right">128.48</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.55</td>
    <td align="right">25.84</td>
    <td align="right">26.52</td>
    <td align="right">31.61</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">31.57</td>
    <td align="right">30.12</td>
    <td align="right">29.93</td>
    <td align="right">33.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">157.71</td>
    <td align="right">161.34</td>
    <td align="right">163.83</td>
    <td align="right">168.32</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">27.03</td>
    <td align="right">27.28</td>
    <td align="right">27.76</td>
    <td align="right">34.27</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">32.14</td>
    <td align="right">32.09</td>
    <td align="right">31.68</td>
    <td align="right">35.13</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.66</td>
    <td align="right">43.36</td>
    <td align="right">33.28</td>
    <td align="right">38.96</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.60</td>
    <td align="right">43.46</td>
    <td align="right">34.71</td>
    <td align="right">39.43</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.66</td>
    <td align="right">29.00</td>
    <td align="right">28.96</td>
    <td align="right">32.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.55</td>
    <td align="right">58.76</td>
    <td align="right">34.01</td>
    <td align="right">46.44</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.13</td>
    <td align="right">58.94</td>
    <td align="right">36.26</td>
    <td align="right">47.88</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.85</td>
    <td align="right">37.83</td>
    <td align="right">27.94</td>
    <td align="right">37.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.00</td>
    <td align="right">78.51</td>
    <td align="right">36.10</td>
    <td align="right">56.93</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.45</td>
    <td align="right">79.13</td>
    <td align="right">37.14</td>
    <td align="right">58.30</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.15</td>
    <td align="right">53.94</td>
    <td align="right">37.29</td>
    <td align="right">50.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.31</td>
    <td align="right">88.22</td>
    <td align="right">34.69</td>
    <td align="right">63.03</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.53</td>
    <td align="right">96.25</td>
    <td align="right">39.10</td>
    <td align="right">67.36</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.94</td>
    <td align="right">54.62</td>
    <td align="right">37.73</td>
    <td align="right">50.52</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.62</td>
    <td align="right">42.39</td>
    <td align="right">42.34</td>
    <td align="right">44.34</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.56</td>
    <td align="right">42.25</td>
    <td align="right">42.48</td>
    <td align="right">44.58</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.68</td>
    <td align="right">29.84</td>
    <td align="right">30.12</td>
    <td align="right">33.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.61</td>
    <td align="right">56.73</td>
    <td align="right">56.32</td>
    <td align="right">58.83</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.09</td>
    <td align="right">56.53</td>
    <td align="right">56.41</td>
    <td align="right">59.59</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.90</td>
    <td align="right">37.32</td>
    <td align="right">37.04</td>
    <td align="right">37.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.11</td>
    <td align="right">76.32</td>
    <td align="right">76.04</td>
    <td align="right">80.86</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.16</td>
    <td align="right">76.44</td>
    <td align="right">76.46</td>
    <td align="right">78.90</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">29.68</td>
    <td align="right">49.31</td>
    <td align="right">49.10</td>
    <td align="right">52.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">43.66</td>
    <td align="right">85.44</td>
    <td align="right">84.85</td>
    <td align="right">90.21</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.14</td>
    <td align="right">91.39</td>
    <td align="right">90.91</td>
    <td align="right">94.18</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">28.86</td>
    <td align="right">49.54</td>
    <td align="right">49.25</td>
    <td align="right">53.08</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.60</td>
    <td align="right">43.10</td>
    <td align="right">33.67</td>
    <td align="right">38.51</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.51</td>
    <td align="right">42.80</td>
    <td align="right">35.08</td>
    <td align="right">39.58</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.38</td>
    <td align="right">28.00</td>
    <td align="right">27.47</td>
    <td align="right">31.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.61</td>
    <td align="right">58.72</td>
    <td align="right">35.02</td>
    <td align="right">47.63</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.33</td>
    <td align="right">58.92</td>
    <td align="right">37.60</td>
    <td align="right">48.66</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.88</td>
    <td align="right">37.70</td>
    <td align="right">27.92</td>
    <td align="right">37.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">39.61</td>
    <td align="right">77.97</td>
    <td align="right">35.84</td>
    <td align="right">56.70</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.93</td>
    <td align="right">78.37</td>
    <td align="right">37.53</td>
    <td align="right">58.31</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">28.23</td>
    <td align="right">48.07</td>
    <td align="right">30.96</td>
    <td align="right">43.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">42.22</td>
    <td align="right">88.05</td>
    <td align="right">35.24</td>
    <td align="right">62.23</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.43</td>
    <td align="right">96.30</td>
    <td align="right">38.17</td>
    <td align="right">68.36</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.15</td>
    <td align="right">48.22</td>
    <td align="right">31.26</td>
    <td align="right">44.02</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.29</td>
    <td align="right">41.05</td>
    <td align="right">41.35</td>
    <td align="right">43.91</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.43</td>
    <td align="right">41.01</td>
    <td align="right">41.70</td>
    <td align="right">44.34</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.41</td>
    <td align="right">28.99</td>
    <td align="right">29.19</td>
    <td align="right">32.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.56</td>
    <td align="right">55.47</td>
    <td align="right">55.80</td>
    <td align="right">58.42</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.29</td>
    <td align="right">55.86</td>
    <td align="right">56.23</td>
    <td align="right">58.95</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.89</td>
    <td align="right">37.61</td>
    <td align="right">37.58</td>
    <td align="right">37.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">39.18</td>
    <td align="right">74.90</td>
    <td align="right">75.20</td>
    <td align="right">77.48</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.51</td>
    <td align="right">75.08</td>
    <td align="right">75.31</td>
    <td align="right">78.10</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">28.04</td>
    <td align="right">48.64</td>
    <td align="right">48.58</td>
    <td align="right">52.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">42.56</td>
    <td align="right">83.94</td>
    <td align="right">84.14</td>
    <td align="right">86.74</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.43</td>
    <td align="right">90.41</td>
    <td align="right">90.09</td>
    <td align="right">93.02</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">28.22</td>
    <td align="right">49.17</td>
    <td align="right">49.10</td>
    <td align="right">53.27</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.96</td>
    <td align="right">29.07</td>
    <td align="right">29.02</td>
    <td align="right">32.95</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.87</td>
    <td align="right">31.09</td>
    <td align="right">30.95</td>
    <td align="right">34.88</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.36</td>
    <td align="right">30.88</td>
    <td align="right">30.34</td>
    <td align="right">34.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.06</td>
    <td align="right">44.69</td>
    <td align="right">34.68</td>
    <td align="right">44.67</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.91</td>
    <td align="right">39.18</td>
    <td align="right">29.47</td>
    <td align="right">38.93</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.75</td>
    <td align="right">46.98</td>
    <td align="right">37.88</td>
    <td align="right">47.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.12</td>
    <td align="right">53.82</td>
    <td align="right">36.99</td>
    <td align="right">49.86</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">35.45</td>
    <td align="right">57.56</td>
    <td align="right">40.06</td>
    <td align="right">53.54</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.35</td>
    <td align="right">57.66</td>
    <td align="right">39.61</td>
    <td align="right">53.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.61</td>
    <td align="right">54.19</td>
    <td align="right">37.43</td>
    <td align="right">50.43</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">34.12</td>
    <td align="right">59.48</td>
    <td align="right">40.42</td>
    <td align="right">54.62</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.95</td>
    <td align="right">58.93</td>
    <td align="right">40.03</td>
    <td align="right">54.56</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.94</td>
    <td align="right">29.87</td>
    <td align="right">30.22</td>
    <td align="right">33.47</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.85</td>
    <td align="right">30.14</td>
    <td align="right">29.91</td>
    <td align="right">33.74</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.42</td>
    <td align="right">29.98</td>
    <td align="right">29.87</td>
    <td align="right">34.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.04</td>
    <td align="right">38.38</td>
    <td align="right">37.75</td>
    <td align="right">38.29</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.94</td>
    <td align="right">37.88</td>
    <td align="right">37.89</td>
    <td align="right">38.51</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.75</td>
    <td align="right">38.47</td>
    <td align="right">38.76</td>
    <td align="right">39.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.26</td>
    <td align="right">48.78</td>
    <td align="right">48.84</td>
    <td align="right">51.98</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">33.76</td>
    <td align="right">51.62</td>
    <td align="right">51.67</td>
    <td align="right">55.23</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.99</td>
    <td align="right">51.67</td>
    <td align="right">51.26</td>
    <td align="right">55.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">30.64</td>
    <td align="right">48.96</td>
    <td align="right">48.79</td>
    <td align="right">52.28</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">33.17</td>
    <td align="right">53.31</td>
    <td align="right">53.13</td>
    <td align="right">57.18</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">37.28</td>
    <td align="right">53.44</td>
    <td align="right">52.87</td>
    <td align="right">56.86</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.85</td>
    <td align="right">27.53</td>
    <td align="right">27.14</td>
    <td align="right">31.87</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.84</td>
    <td align="right">29.42</td>
    <td align="right">29.51</td>
    <td align="right">33.87</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.41</td>
    <td align="right">29.32</td>
    <td align="right">29.41</td>
    <td align="right">33.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.98</td>
    <td align="right">39.68</td>
    <td align="right">29.64</td>
    <td align="right">39.70</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.72</td>
    <td align="right">39.13</td>
    <td align="right">29.53</td>
    <td align="right">39.00</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.88</td>
    <td align="right">41.10</td>
    <td align="right">31.08</td>
    <td align="right">41.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">27.99</td>
    <td align="right">47.14</td>
    <td align="right">30.12</td>
    <td align="right">43.23</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">32.33</td>
    <td align="right">50.60</td>
    <td align="right">32.95</td>
    <td align="right">46.36</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">33.95</td>
    <td align="right">49.87</td>
    <td align="right">32.38</td>
    <td align="right">45.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.42</td>
    <td align="right">47.08</td>
    <td align="right">30.40</td>
    <td align="right">43.47</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.66</td>
    <td align="right">52.37</td>
    <td align="right">32.90</td>
    <td align="right">47.03</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.34</td>
    <td align="right">51.57</td>
    <td align="right">32.42</td>
    <td align="right">46.74</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.86</td>
    <td align="right">28.99</td>
    <td align="right">28.96</td>
    <td align="right">32.79</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.87</td>
    <td align="right">29.48</td>
    <td align="right">29.41</td>
    <td align="right">34.03</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.42</td>
    <td align="right">29.24</td>
    <td align="right">29.19</td>
    <td align="right">34.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.95</td>
    <td align="right">38.53</td>
    <td align="right">39.72</td>
    <td align="right">40.76</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.75</td>
    <td align="right">37.95</td>
    <td align="right">37.98</td>
    <td align="right">38.77</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.93</td>
    <td align="right">39.19</td>
    <td align="right">38.57</td>
    <td align="right">39.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.02</td>
    <td align="right">48.69</td>
    <td align="right">48.64</td>
    <td align="right">52.37</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.28</td>
    <td align="right">51.41</td>
    <td align="right">51.06</td>
    <td align="right">54.97</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.31</td>
    <td align="right">51.24</td>
    <td align="right">51.15</td>
    <td align="right">55.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">32.17</td>
    <td align="right">48.85</td>
    <td align="right">48.58</td>
    <td align="right">52.51</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">35.22</td>
    <td align="right">53.03</td>
    <td align="right">52.79</td>
    <td align="right">56.76</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">35.53</td>
    <td align="right">52.84</td>
    <td align="right">52.69</td>
    <td align="right">56.43</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.02</td>
    <td align="right">44.26</td>
    <td align="right">32.72</td>
    <td align="right">38.66</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.62</td>
    <td align="right">56.74</td>
    <td align="right">37.03</td>
    <td align="right">46.70</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.43</td>
    <td align="right">64.37</td>
    <td align="right">38.67</td>
    <td align="right">50.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.63</td>
    <td align="right">61.79</td>
    <td align="right">33.67</td>
    <td align="right">48.46</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.37</td>
    <td align="right">62.41</td>
    <td align="right">35.42</td>
    <td align="right">49.71</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">45.73</td>
    <td align="right">82.70</td>
    <td align="right">40.37</td>
    <td align="right">60.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.90</td>
    <td align="right">74.44</td>
    <td align="right">33.59</td>
    <td align="right">55.08</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.97</td>
    <td align="right">79.00</td>
    <td align="right">36.66</td>
    <td align="right">58.44</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.35</td>
    <td align="right">89.37</td>
    <td align="right">39.07</td>
    <td align="right">63.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.50</td>
    <td align="right">102.05</td>
    <td align="right">34.59</td>
    <td align="right">68.32</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.80</td>
    <td align="right">100.18</td>
    <td align="right">36.38</td>
    <td align="right">69.03</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.90</td>
    <td align="right">119.99</td>
    <td align="right">40.16</td>
    <td align="right">80.26</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.06</td>
    <td align="right">42.97</td>
    <td align="right">42.77</td>
    <td align="right">46.81</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.65</td>
    <td align="right">48.56</td>
    <td align="right">48.32</td>
    <td align="right">51.10</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.21</td>
    <td align="right">60.65</td>
    <td align="right">60.92</td>
    <td align="right">65.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.80</td>
    <td align="right">57.08</td>
    <td align="right">56.13</td>
    <td align="right">59.67</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.36</td>
    <td align="right">60.33</td>
    <td align="right">60.29</td>
    <td align="right">63.87</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">45.59</td>
    <td align="right">79.31</td>
    <td align="right">80.42</td>
    <td align="right">83.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">41.04</td>
    <td align="right">68.10</td>
    <td align="right">67.33</td>
    <td align="right">70.33</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.99</td>
    <td align="right">78.37</td>
    <td align="right">77.61</td>
    <td align="right">80.37</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">48.67</td>
    <td align="right">86.28</td>
    <td align="right">85.70</td>
    <td align="right">88.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">53.63</td>
    <td align="right">91.34</td>
    <td align="right">92.14</td>
    <td align="right">95.13</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.77</td>
    <td align="right">92.01</td>
    <td align="right">91.48</td>
    <td align="right">96.63</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.51</td>
    <td align="right">117.51</td>
    <td align="right">116.75</td>
    <td align="right">120.84</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">28.23</td>
    <td align="right">44.40</td>
    <td align="right">34.40</td>
    <td align="right">39.99</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.89</td>
    <td align="right">56.61</td>
    <td align="right">38.46</td>
    <td align="right">46.98</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.38</td>
    <td align="right">64.55</td>
    <td align="right">39.86</td>
    <td align="right">52.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">38.04</td>
    <td align="right">61.96</td>
    <td align="right">35.66</td>
    <td align="right">49.48</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.19</td>
    <td align="right">63.00</td>
    <td align="right">36.03</td>
    <td align="right">49.75</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.22</td>
    <td align="right">82.18</td>
    <td align="right">40.05</td>
    <td align="right">62.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.62</td>
    <td align="right">73.89</td>
    <td align="right">35.08</td>
    <td align="right">55.85</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.24</td>
    <td align="right">79.24</td>
    <td align="right">37.18</td>
    <td align="right">58.81</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">50.72</td>
    <td align="right">92.60</td>
    <td align="right">37.97</td>
    <td align="right">66.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.50</td>
    <td align="right">99.47</td>
    <td align="right">36.69</td>
    <td align="right">68.98</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.69</td>
    <td align="right">99.62</td>
    <td align="right">36.45</td>
    <td align="right">71.33</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.40</td>
    <td align="right">120.63</td>
    <td align="right">38.95</td>
    <td align="right">81.03</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">28.56</td>
    <td align="right">42.63</td>
    <td align="right">43.13</td>
    <td align="right">45.68</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.80</td>
    <td align="right">48.11</td>
    <td align="right">48.19</td>
    <td align="right">50.32</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.39</td>
    <td align="right">60.36</td>
    <td align="right">61.08</td>
    <td align="right">63.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">37.99</td>
    <td align="right">56.37</td>
    <td align="right">57.18</td>
    <td align="right">59.34</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.26</td>
    <td align="right">59.47</td>
    <td align="right">59.47</td>
    <td align="right">61.99</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.29</td>
    <td align="right">78.15</td>
    <td align="right">77.59</td>
    <td align="right">81.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.48</td>
    <td align="right">67.50</td>
    <td align="right">67.34</td>
    <td align="right">69.91</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.10</td>
    <td align="right">76.60</td>
    <td align="right">77.06</td>
    <td align="right">79.84</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.50</td>
    <td align="right">84.39</td>
    <td align="right">84.12</td>
    <td align="right">87.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">56.10</td>
    <td align="right">91.94</td>
    <td align="right">91.66</td>
    <td align="right">96.69</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.69</td>
    <td align="right">92.10</td>
    <td align="right">91.11</td>
    <td align="right">96.33</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">66.08</td>
    <td align="right">118.07</td>
    <td align="right">117.48</td>
    <td align="right">122.10</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">65.13</td>
    <td align="right">33.97</td>
    <td align="right">21.09</td>
    <td align="right">37.71</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">93.31</td>
    <td align="right">61.92</td>
    <td align="right">41.91</td>
    <td align="right">51.69</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.08</td>
    <td align="right">26.12</td>
    <td align="right">29.21</td>
    <td align="right">31.56</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">28.17</td>
    <td align="right">27.19</td>
    <td align="right">28.09</td>
    <td align="right">30.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">157.66</td>
    <td align="right">151.38</td>
    <td align="right">57.89</td>
    <td align="right">104.80</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.65</td>
    <td align="right">24.93</td>
    <td align="right">25.95</td>
    <td align="right">29.45</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">33.43</td>
    <td align="right">31.11</td>
    <td align="right">30.48</td>
    <td align="right">33.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">257.94</td>
    <td align="right">214.24</td>
    <td align="right">63.36</td>
    <td align="right">140.19</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.91</td>
    <td align="right">38.26</td>
    <td align="right">38.75</td>
    <td align="right">43.08</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.22</td>
    <td align="right">47.98</td>
    <td align="right">47.55</td>
    <td align="right">50.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">436.58</td>
    <td align="right">352.03</td>
    <td align="right">78.58</td>
    <td align="right">218.32</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.22</td>
    <td align="right">44.86</td>
    <td align="right">45.68</td>
    <td align="right">50.50</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.49</td>
    <td align="right">62.11</td>
    <td align="right">63.75</td>
    <td align="right">65.76</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">89.82</td>
    <td align="right">65.18</td>
    <td align="right">65.58</td>
    <td align="right">71.73</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">22.10</td>
    <td align="right">21.25</td>
    <td align="right">24.33</td>
    <td align="right">26.61</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">27.76</td>
    <td align="right">27.15</td>
    <td align="right">28.13</td>
    <td align="right">29.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">140.67</td>
    <td align="right">138.36</td>
    <td align="right">138.53</td>
    <td align="right">145.58</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">33.62</td>
    <td align="right">33.41</td>
    <td align="right">34.39</td>
    <td align="right">38.48</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">31.45</td>
    <td align="right">31.02</td>
    <td align="right">30.83</td>
    <td align="right">32.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">264.70</td>
    <td align="right">227.49</td>
    <td align="right">227.46</td>
    <td align="right">234.49</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.71</td>
    <td align="right">38.05</td>
    <td align="right">38.51</td>
    <td align="right">42.66</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">49.07</td>
    <td align="right">50.26</td>
    <td align="right">49.66</td>
    <td align="right">52.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">436.86</td>
    <td align="right">360.76</td>
    <td align="right">360.54</td>
    <td align="right">367.07</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">44.89</td>
    <td align="right">44.69</td>
    <td align="right">45.71</td>
    <td align="right">50.42</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.99</td>
    <td align="right">62.19</td>
    <td align="right">63.85</td>
    <td align="right">65.54</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">95.35</td>
    <td align="right">113.00</td>
    <td align="right">64.13</td>
    <td align="right">88.11</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">22.38</td>
    <td align="right">22.05</td>
    <td align="right">24.83</td>
    <td align="right">28.35</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">29.32</td>
    <td align="right">35.65</td>
    <td align="right">37.05</td>
    <td align="right">38.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">140.07</td>
    <td align="right">156.59</td>
    <td align="right">64.13</td>
    <td align="right">110.16</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.18</td>
    <td align="right">25.55</td>
    <td align="right">27.28</td>
    <td align="right">31.96</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">32.79</td>
    <td align="right">37.48</td>
    <td align="right">38.23</td>
    <td align="right">40.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">258.05</td>
    <td align="right">241.84</td>
    <td align="right">75.04</td>
    <td align="right">157.66</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">42.51</td>
    <td align="right">42.23</td>
    <td align="right">43.62</td>
    <td align="right">49.72</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.07</td>
    <td align="right">48.42</td>
    <td align="right">48.24</td>
    <td align="right">50.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">437.46</td>
    <td align="right">422.63</td>
    <td align="right">96.02</td>
    <td align="right">258.48</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">53.74</td>
    <td align="right">54.29</td>
    <td align="right">54.85</td>
    <td align="right">61.45</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.95</td>
    <td align="right">62.58</td>
    <td align="right">61.70</td>
    <td align="right">64.63</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.80</td>
    <td align="right">71.83</td>
    <td align="right">71.85</td>
    <td align="right">78.07</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.25</td>
    <td align="right">22.06</td>
    <td align="right">25.26</td>
    <td align="right">28.57</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">27.59</td>
    <td align="right">31.91</td>
    <td align="right">33.30</td>
    <td align="right">34.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">132.88</td>
    <td align="right">127.89</td>
    <td align="right">127.31</td>
    <td align="right">133.85</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.75</td>
    <td align="right">27.71</td>
    <td align="right">29.42</td>
    <td align="right">34.25</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">33.64</td>
    <td align="right">31.76</td>
    <td align="right">32.35</td>
    <td align="right">34.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">265.98</td>
    <td align="right">261.09</td>
    <td align="right">260.85</td>
    <td align="right">265.59</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">42.25</td>
    <td align="right">42.20</td>
    <td align="right">42.78</td>
    <td align="right">49.05</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.16</td>
    <td align="right">49.22</td>
    <td align="right">48.69</td>
    <td align="right">51.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">440.99</td>
    <td align="right">435.78</td>
    <td align="right">436.39</td>
    <td align="right">440.92</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">54.16</td>
    <td align="right">54.35</td>
    <td align="right">55.40</td>
    <td align="right">62.68</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.43</td>
    <td align="right">62.39</td>
    <td align="right">61.44</td>
    <td align="right">64.40</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">27.82</td>
    <td align="right">52.98</td>
    <td align="right">44.47</td>
    <td align="right">49.44</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">32.15</td>
    <td align="right">43.74</td>
    <td align="right">36.32</td>
    <td align="right">40.43</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.06</td>
    <td align="right">31.29</td>
    <td align="right">31.29</td>
    <td align="right">35.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.08</td>
    <td align="right">66.54</td>
    <td align="right">44.74</td>
    <td align="right">55.97</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">38.14</td>
    <td align="right">61.89</td>
    <td align="right">40.76</td>
    <td align="right">51.99</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">20.04</td>
    <td align="right">41.21</td>
    <td align="right">31.32</td>
    <td align="right">41.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">60.29</td>
    <td align="right">94.34</td>
    <td align="right">54.10</td>
    <td align="right">74.42</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.66</td>
    <td align="right">96.23</td>
    <td align="right">57.91</td>
    <td align="right">77.26</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">47.18</td>
    <td align="right">78.63</td>
    <td align="right">61.73</td>
    <td align="right">75.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.15</td>
    <td align="right">111.76</td>
    <td align="right">60.92</td>
    <td align="right">88.15</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.83</td>
    <td align="right">126.61</td>
    <td align="right">74.53</td>
    <td align="right">100.38</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.51</td>
    <td align="right">91.08</td>
    <td align="right">74.09</td>
    <td align="right">87.59</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.14</td>
    <td align="right">42.96</td>
    <td align="right">42.64</td>
    <td align="right">44.93</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.59</td>
    <td align="right">42.25</td>
    <td align="right">42.39</td>
    <td align="right">44.57</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">19.02</td>
    <td align="right">31.89</td>
    <td align="right">32.47</td>
    <td align="right">36.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.99</td>
    <td align="right">58.92</td>
    <td align="right">58.86</td>
    <td align="right">61.38</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">40.28</td>
    <td align="right">68.96</td>
    <td align="right">68.96</td>
    <td align="right">72.16</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.32</td>
    <td align="right">40.80</td>
    <td align="right">40.41</td>
    <td align="right">41.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.32</td>
    <td align="right">89.38</td>
    <td align="right">89.54</td>
    <td align="right">94.11</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">63.17</td>
    <td align="right">92.39</td>
    <td align="right">92.48</td>
    <td align="right">95.00</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.34</td>
    <td align="right">73.79</td>
    <td align="right">74.18</td>
    <td align="right">77.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">74.83</td>
    <td align="right">108.05</td>
    <td align="right">107.84</td>
    <td align="right">112.49</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.59</td>
    <td align="right">120.32</td>
    <td align="right">119.81</td>
    <td align="right">122.98</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.74</td>
    <td align="right">87.15</td>
    <td align="right">87.19</td>
    <td align="right">90.19</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">27.57</td>
    <td align="right">42.67</td>
    <td align="right">34.95</td>
    <td align="right">39.70</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.17</td>
    <td align="right">53.44</td>
    <td align="right">49.54</td>
    <td align="right">52.12</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">17.84</td>
    <td align="right">29.67</td>
    <td align="right">29.52</td>
    <td align="right">34.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.74</td>
    <td align="right">61.98</td>
    <td align="right">40.54</td>
    <td align="right">52.28</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.79</td>
    <td align="right">62.29</td>
    <td align="right">43.25</td>
    <td align="right">52.44</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.61</td>
    <td align="right">40.81</td>
    <td align="right">30.67</td>
    <td align="right">40.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">60.59</td>
    <td align="right">92.53</td>
    <td align="right">52.96</td>
    <td align="right">72.70</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">65.12</td>
    <td align="right">95.84</td>
    <td align="right">59.39</td>
    <td align="right">77.95</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">49.22</td>
    <td align="right">72.84</td>
    <td align="right">56.27</td>
    <td align="right">69.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">77.92</td>
    <td align="right">114.44</td>
    <td align="right">62.12</td>
    <td align="right">87.89</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.42</td>
    <td align="right">126.36</td>
    <td align="right">73.96</td>
    <td align="right">101.02</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">61.22</td>
    <td align="right">85.80</td>
    <td align="right">68.71</td>
    <td align="right">81.26</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">27.12</td>
    <td align="right">41.10</td>
    <td align="right">41.32</td>
    <td align="right">43.90</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.91</td>
    <td align="right">48.43</td>
    <td align="right">48.96</td>
    <td align="right">52.09</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.28</td>
    <td align="right">30.84</td>
    <td align="right">31.07</td>
    <td align="right">34.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.34</td>
    <td align="right">58.75</td>
    <td align="right">59.38</td>
    <td align="right">61.71</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.13</td>
    <td align="right">67.36</td>
    <td align="right">67.54</td>
    <td align="right">70.23</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.24</td>
    <td align="right">40.86</td>
    <td align="right">40.35</td>
    <td align="right">41.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">60.96</td>
    <td align="right">90.21</td>
    <td align="right">90.45</td>
    <td align="right">92.92</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.93</td>
    <td align="right">92.39</td>
    <td align="right">92.95</td>
    <td align="right">95.23</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">49.41</td>
    <td align="right">72.70</td>
    <td align="right">72.79</td>
    <td align="right">77.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">77.69</td>
    <td align="right">107.74</td>
    <td align="right">108.10</td>
    <td align="right">110.95</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.11</td>
    <td align="right">119.36</td>
    <td align="right">119.42</td>
    <td align="right">122.10</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">60.85</td>
    <td align="right">86.17</td>
    <td align="right">86.63</td>
    <td align="right">91.10</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.41</td>
    <td align="right">30.73</td>
    <td align="right">30.66</td>
    <td align="right">34.94</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">21.02</td>
    <td align="right">32.46</td>
    <td align="right">32.42</td>
    <td align="right">36.69</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">21.98</td>
    <td align="right">32.07</td>
    <td align="right">32.01</td>
    <td align="right">36.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.46</td>
    <td align="right">49.57</td>
    <td align="right">39.47</td>
    <td align="right">50.21</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">27.07</td>
    <td align="right">50.55</td>
    <td align="right">40.65</td>
    <td align="right">50.44</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.57</td>
    <td align="right">51.52</td>
    <td align="right">43.30</td>
    <td align="right">52.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.92</td>
    <td align="right">78.17</td>
    <td align="right">61.12</td>
    <td align="right">74.46</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">51.91</td>
    <td align="right">81.09</td>
    <td align="right">63.61</td>
    <td align="right">77.05</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">52.62</td>
    <td align="right">81.05</td>
    <td align="right">63.15</td>
    <td align="right">77.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.52</td>
    <td align="right">92.62</td>
    <td align="right">74.87</td>
    <td align="right">88.24</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">62.99</td>
    <td align="right">96.53</td>
    <td align="right">77.65</td>
    <td align="right">91.81</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.90</td>
    <td align="right">98.18</td>
    <td align="right">78.43</td>
    <td align="right">93.66</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.18</td>
    <td align="right">31.58</td>
    <td align="right">31.90</td>
    <td align="right">35.39</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.05</td>
    <td align="right">42.58</td>
    <td align="right">42.59</td>
    <td align="right">46.83</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">21.36</td>
    <td align="right">31.22</td>
    <td align="right">31.09</td>
    <td align="right">35.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.09</td>
    <td align="right">41.85</td>
    <td align="right">41.00</td>
    <td align="right">41.52</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.05</td>
    <td align="right">40.64</td>
    <td align="right">40.58</td>
    <td align="right">41.75</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.87</td>
    <td align="right">41.25</td>
    <td align="right">42.07</td>
    <td align="right">42.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.66</td>
    <td align="right">73.74</td>
    <td align="right">73.86</td>
    <td align="right">76.66</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">54.29</td>
    <td align="right">76.83</td>
    <td align="right">76.71</td>
    <td align="right">80.69</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.03</td>
    <td align="right">74.39</td>
    <td align="right">74.05</td>
    <td align="right">78.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.95</td>
    <td align="right">88.06</td>
    <td align="right">87.96</td>
    <td align="right">90.29</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.01</td>
    <td align="right">90.35</td>
    <td align="right">90.16</td>
    <td align="right">94.54</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.57</td>
    <td align="right">91.14</td>
    <td align="right">90.73</td>
    <td align="right">95.26</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.24</td>
    <td align="right">28.77</td>
    <td align="right">28.75</td>
    <td align="right">33.69</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.05</td>
    <td align="right">30.46</td>
    <td align="right">30.49</td>
    <td align="right">35.14</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.65</td>
    <td align="right">30.32</td>
    <td align="right">30.33</td>
    <td align="right">34.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">22.01</td>
    <td align="right">44.97</td>
    <td align="right">34.84</td>
    <td align="right">45.71</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.60</td>
    <td align="right">42.26</td>
    <td align="right">32.62</td>
    <td align="right">42.18</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">26.03</td>
    <td align="right">47.02</td>
    <td align="right">36.89</td>
    <td align="right">47.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.17</td>
    <td align="right">71.30</td>
    <td align="right">54.59</td>
    <td align="right">67.62</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.05</td>
    <td align="right">73.90</td>
    <td align="right">55.81</td>
    <td align="right">69.20</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">51.84</td>
    <td align="right">71.59</td>
    <td align="right">54.33</td>
    <td align="right">67.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.60</td>
    <td align="right">85.05</td>
    <td align="right">68.50</td>
    <td align="right">81.41</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">65.74</td>
    <td align="right">89.09</td>
    <td align="right">69.69</td>
    <td align="right">83.49</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.49</td>
    <td align="right">89.11</td>
    <td align="right">70.07</td>
    <td align="right">84.01</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.28</td>
    <td align="right">30.64</td>
    <td align="right">30.52</td>
    <td align="right">34.80</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.97</td>
    <td align="right">30.76</td>
    <td align="right">30.61</td>
    <td align="right">35.36</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">21.57</td>
    <td align="right">30.72</td>
    <td align="right">30.63</td>
    <td align="right">35.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">22.26</td>
    <td align="right">43.42</td>
    <td align="right">43.30</td>
    <td align="right">44.25</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.31</td>
    <td align="right">48.79</td>
    <td align="right">48.57</td>
    <td align="right">49.63</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">25.26</td>
    <td align="right">42.57</td>
    <td align="right">42.14</td>
    <td align="right">44.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.50</td>
    <td align="right">72.76</td>
    <td align="right">73.30</td>
    <td align="right">77.38</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.92</td>
    <td align="right">76.17</td>
    <td align="right">75.87</td>
    <td align="right">79.75</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">52.66</td>
    <td align="right">76.08</td>
    <td align="right">76.07</td>
    <td align="right">80.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.47</td>
    <td align="right">86.49</td>
    <td align="right">86.92</td>
    <td align="right">90.59</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">65.66</td>
    <td align="right">92.06</td>
    <td align="right">92.13</td>
    <td align="right">95.73</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.30</td>
    <td align="right">92.60</td>
    <td align="right">93.03</td>
    <td align="right">96.60</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">29.32</td>
    <td align="right">44.44</td>
    <td align="right">34.38</td>
    <td align="right">39.99</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">38.34</td>
    <td align="right">56.74</td>
    <td align="right">39.22</td>
    <td align="right">47.62</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">41.55</td>
    <td align="right">64.23</td>
    <td align="right">40.49</td>
    <td align="right">51.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.08</td>
    <td align="right">68.81</td>
    <td align="right">42.96</td>
    <td align="right">57.11</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">48.31</td>
    <td align="right">64.48</td>
    <td align="right">38.64</td>
    <td align="right">52.84</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">50.02</td>
    <td align="right">87.94</td>
    <td align="right">44.87</td>
    <td align="right">65.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.78</td>
    <td align="right">87.08</td>
    <td align="right">50.62</td>
    <td align="right">70.39</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.41</td>
    <td align="right">99.93</td>
    <td align="right">60.58</td>
    <td align="right">81.00</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">75.87</td>
    <td align="right">107.57</td>
    <td align="right">52.43</td>
    <td align="right">79.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">79.34</td>
    <td align="right">122.99</td>
    <td align="right">62.42</td>
    <td align="right">92.97</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">92.86</td>
    <td align="right">132.43</td>
    <td align="right">73.11</td>
    <td align="right">104.04</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">108.23</td>
    <td align="right">148.88</td>
    <td align="right">63.34</td>
    <td align="right">106.49</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.68</td>
    <td align="right">43.06</td>
    <td align="right">42.58</td>
    <td align="right">46.54</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">39.04</td>
    <td align="right">48.97</td>
    <td align="right">48.63</td>
    <td align="right">51.21</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">41.29</td>
    <td align="right">60.78</td>
    <td align="right">60.87</td>
    <td align="right">65.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.02</td>
    <td align="right">62.72</td>
    <td align="right">61.94</td>
    <td align="right">65.43</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">49.17</td>
    <td align="right">72.12</td>
    <td align="right">72.15</td>
    <td align="right">75.45</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">53.41</td>
    <td align="right">80.68</td>
    <td align="right">81.89</td>
    <td align="right">84.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">59.49</td>
    <td align="right">76.96</td>
    <td align="right">76.42</td>
    <td align="right">79.60</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.85</td>
    <td align="right">104.53</td>
    <td align="right">103.89</td>
    <td align="right">106.74</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">75.13</td>
    <td align="right">103.96</td>
    <td align="right">103.70</td>
    <td align="right">106.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">80.27</td>
    <td align="right">110.92</td>
    <td align="right">110.69</td>
    <td align="right">113.70</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.14</td>
    <td align="right">126.26</td>
    <td align="right">126.18</td>
    <td align="right">130.99</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.80</td>
    <td align="right">144.97</td>
    <td align="right">144.67</td>
    <td align="right">149.01</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">32.61</td>
    <td align="right">52.06</td>
    <td align="right">44.72</td>
    <td align="right">49.30</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">40.38</td>
    <td align="right">56.53</td>
    <td align="right">41.69</td>
    <td align="right">48.11</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">47.25</td>
    <td align="right">64.82</td>
    <td align="right">42.61</td>
    <td align="right">53.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">45.93</td>
    <td align="right">64.77</td>
    <td align="right">39.41</td>
    <td align="right">53.02</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">49.74</td>
    <td align="right">72.21</td>
    <td align="right">48.94</td>
    <td align="right">60.77</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">53.98</td>
    <td align="right">86.15</td>
    <td align="right">42.77</td>
    <td align="right">64.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.70</td>
    <td align="right">88.27</td>
    <td align="right">53.79</td>
    <td align="right">72.21</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">74.43</td>
    <td align="right">100.86</td>
    <td align="right">64.19</td>
    <td align="right">82.55</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">76.56</td>
    <td align="right">114.21</td>
    <td align="right">48.50</td>
    <td align="right">84.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.87</td>
    <td align="right">121.85</td>
    <td align="right">64.58</td>
    <td align="right">94.47</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">95.33</td>
    <td align="right">133.77</td>
    <td align="right">74.54</td>
    <td align="right">106.67</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">117.97</td>
    <td align="right">161.86</td>
    <td align="right">47.37</td>
    <td align="right">112.02</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">33.40</td>
    <td align="right">48.71</td>
    <td align="right">48.71</td>
    <td align="right">51.72</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.92</td>
    <td align="right">47.98</td>
    <td align="right">48.21</td>
    <td align="right">50.73</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">47.58</td>
    <td align="right">60.57</td>
    <td align="right">61.43</td>
    <td align="right">63.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">45.67</td>
    <td align="right">59.02</td>
    <td align="right">59.46</td>
    <td align="right">61.87</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">49.24</td>
    <td align="right">64.71</td>
    <td align="right">64.42</td>
    <td align="right">67.18</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">55.01</td>
    <td align="right">88.76</td>
    <td align="right">88.13</td>
    <td align="right">92.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.77</td>
    <td align="right">78.86</td>
    <td align="right">79.11</td>
    <td align="right">81.72</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.18</td>
    <td align="right">101.61</td>
    <td align="right">100.84</td>
    <td align="right">106.08</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">78.71</td>
    <td align="right">106.14</td>
    <td align="right">105.23</td>
    <td align="right">110.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.85</td>
    <td align="right">113.71</td>
    <td align="right">113.06</td>
    <td align="right">118.37</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">95.49</td>
    <td align="right">126.97</td>
    <td align="right">126.48</td>
    <td align="right">130.80</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">117.96</td>
    <td align="right">152.36</td>
    <td align="right">152.23</td>
    <td align="right">159.02</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
