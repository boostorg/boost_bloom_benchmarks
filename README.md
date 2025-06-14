# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.19</td>
    <td align="right">6.25</td>
    <td align="right">4.55</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.51</td>
    <td align="right">11.67</td>
    <td align="right">18.00</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.86</td>
    <td align="right">4.60</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">5.09</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">19.52</td>
    <td align="right">17.40</td>
    <td align="right">18.81</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.41</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.21</td>
    <td align="right">5.47</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.30</td>
    <td align="right">20.06</td>
    <td align="right">17.66</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.00</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.84</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">28.92</td>
    <td align="right">25.11</td>
    <td align="right">18.12</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.60</td>
    <td align="right">5.77</td>
    <td align="right">5.77</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
    <td align="right">6.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.08</td>
    <td align="right">12.19</td>
    <td align="right">18.29</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.81</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.94</td>
    <td align="right">5.12</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.89</td>
    <td align="right">18.03</td>
    <td align="right">19.35</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.29</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.99</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.67</td>
    <td align="right">21.68</td>
    <td align="right">18.51</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.80</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.40</td>
    <td align="right">6.13</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.61</td>
    <td align="right">27.68</td>
    <td align="right">18.64</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.13</td>
    <td align="right">6.07</td>
    <td align="right">6.07</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.89</td>
    <td align="right">6.43</td>
    <td align="right">6.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.19</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.86</td>
    <td align="right">7.08</td>
    <td align="right">7.09</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.24</td>
    <td align="right">3.39</td>
    <td align="right">3.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.09</td>
    <td align="right">7.76</td>
    <td align="right">7.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.20</td>
    <td align="right">9.49</td>
    <td align="right">9.49</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.55</td>
    <td align="right">3.09</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.16</td>
    <td align="right">11.30</td>
    <td align="right">11.21</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">22.41</td>
    <td align="right">13.52</td>
    <td align="right">13.44</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">6.15</td>
    <td align="right">5.84</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.27</td>
    <td align="right">13.07</td>
    <td align="right">13.02</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.10</td>
    <td align="right">15.93</td>
    <td align="right">15.91</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">6.22</td>
    <td align="right">5.88</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">5.68</td>
    <td align="right">5.68</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.91</td>
    <td align="right">6.93</td>
    <td align="right">6.93</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.25</td>
    <td align="right">2.95</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.34</td>
    <td align="right">7.91</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.79</td>
    <td align="right">9.32</td>
    <td align="right">9.32</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">2.76</td>
    <td align="right">2.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.73</td>
    <td align="right">11.19</td>
    <td align="right">11.19</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">21.62</td>
    <td align="right">13.71</td>
    <td align="right">13.70</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">6.10</td>
    <td align="right">6.04</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.58</td>
    <td align="right">13.04</td>
    <td align="right">12.96</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.45</td>
    <td align="right">15.88</td>
    <td align="right">15.76</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">6.15</td>
    <td align="right">6.09</td>
    <td align="right">4.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.21</td>
    <td align="right">3.25</td>
    <td align="right">3.22</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.58</td>
    <td align="right">5.21</td>
    <td align="right">5.26</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.71</td>
    <td align="right">5.03</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.34</td>
    <td align="right">3.33</td>
    <td align="right">3.29</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.40</td>
    <td align="right">4.44</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.76</td>
    <td align="right">5.16</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.61</td>
    <td align="right">5.52</td>
    <td align="right">3.93</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.52</td>
    <td align="right">8.15</td>
    <td align="right">6.23</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.88</td>
    <td align="right">7.91</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.64</td>
    <td align="right">5.55</td>
    <td align="right">3.95</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.10</td>
    <td align="right">9.37</td>
    <td align="right">6.31</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.90</td>
    <td align="right">9.07</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.23</td>
    <td align="right">2.79</td>
    <td align="right">2.76</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.58</td>
    <td align="right">4.85</td>
    <td align="right">4.82</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.72</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.37</td>
    <td align="right">2.86</td>
    <td align="right">2.83</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.52</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.76</td>
    <td align="right">4.75</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.39</td>
    <td align="right">5.67</td>
    <td align="right">3.89</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.17</td>
    <td align="right">8.23</td>
    <td align="right">6.21</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">8.64</td>
    <td align="right">8.01</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.45</td>
    <td align="right">5.71</td>
    <td align="right">3.92</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.92</td>
    <td align="right">9.58</td>
    <td align="right">6.37</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">9.34</td>
    <td align="right">9.18</td>
    <td align="right">6.19</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">48.12</td>
    <td align="right">24.35</td>
    <td align="right">15.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">15.44</td>
    <td align="right">13.44</td>
    <td align="right">19.92</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.60</td>
    <td align="right">6.39</td>
    <td align="right">6.38</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.56</td>
    <td align="right">6.34</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">49.45</td>
    <td align="right">49.00</td>
    <td align="right">25.54</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.93</td>
    <td align="right">10.54</td>
    <td align="right">10.59</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.26</td>
    <td align="right">12.07</td>
    <td align="right">12.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">88.37</td>
    <td align="right">83.63</td>
    <td align="right">31.46</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.44</td>
    <td align="right">17.97</td>
    <td align="right">17.99</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">19.20</td>
    <td align="right">19.15</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">125.77</td>
    <td align="right">116.11</td>
    <td align="right">36.40</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.85</td>
    <td align="right">21.84</td>
    <td align="right">21.83</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.50</td>
    <td align="right">22.63</td>
    <td align="right">22.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.03</td>
    <td align="right">15.70</td>
    <td align="right">20.95</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.69</td>
    <td align="right">5.56</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.52</td>
    <td align="right">5.72</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">51.08</td>
    <td align="right">56.20</td>
    <td align="right">28.28</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.25</td>
    <td align="right">11.37</td>
    <td align="right">11.38</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.27</td>
    <td align="right">12.14</td>
    <td align="right">12.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.17</td>
    <td align="right">94.29</td>
    <td align="right">34.50</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.43</td>
    <td align="right">18.40</td>
    <td align="right">18.40</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.22</td>
    <td align="right">19.12</td>
    <td align="right">19.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.24</td>
    <td align="right">133.84</td>
    <td align="right">40.02</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.35</td>
    <td align="right">21.97</td>
    <td align="right">22.00</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.63</td>
    <td align="right">23.09</td>
    <td align="right">23.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.08</td>
    <td align="right">7.53</td>
    <td align="right">7.52</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.82</td>
    <td align="right">9.24</td>
    <td align="right">9.33</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">5.33</td>
    <td align="right">6.03</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.47</td>
    <td align="right">13.85</td>
    <td align="right">13.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.00</td>
    <td align="right">19.13</td>
    <td align="right">19.16</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.26</td>
    <td align="right">8.30</td>
    <td align="right">8.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">29.56</td>
    <td align="right">29.77</td>
    <td align="right">29.80</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">37.50</td>
    <td align="right">32.74</td>
    <td align="right">32.77</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.34</td>
    <td align="right">20.27</td>
    <td align="right">15.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.08</td>
    <td align="right">38.83</td>
    <td align="right">38.87</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.99</td>
    <td align="right">51.07</td>
    <td align="right">51.07</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">22.33</td>
    <td align="right">23.43</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.30</td>
    <td align="right">7.04</td>
    <td align="right">7.05</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.64</td>
    <td align="right">8.86</td>
    <td align="right">8.89</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.75</td>
    <td align="right">3.42</td>
    <td align="right">3.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.20</td>
    <td align="right">13.61</td>
    <td align="right">13.61</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">17.47</td>
    <td align="right">18.95</td>
    <td align="right">18.89</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.00</td>
    <td align="right">8.33</td>
    <td align="right">8.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.24</td>
    <td align="right">30.03</td>
    <td align="right">30.09</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">38.11</td>
    <td align="right">34.63</td>
    <td align="right">34.65</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">20.20</td>
    <td align="right">20.62</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.37</td>
    <td align="right">39.20</td>
    <td align="right">39.14</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">41.56</td>
    <td align="right">51.37</td>
    <td align="right">51.40</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">24.02</td>
    <td align="right">24.20</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">4.16</td>
    <td align="right">4.11</td>
    <td align="right">4.15</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">6.59</td>
    <td align="right">7.78</td>
    <td align="right">7.76</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.62</td>
    <td align="right">6.15</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.30</td>
    <td align="right">9.16</td>
    <td align="right">9.13</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">7.92</td>
    <td align="right">9.42</td>
    <td align="right">9.39</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.83</td>
    <td align="right">12.80</td>
    <td align="right">13.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">18.03</td>
    <td align="right">18.87</td>
    <td align="right">14.63</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">24.17</td>
    <td align="right">26.62</td>
    <td align="right">21.88</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">25.61</td>
    <td align="right">26.08</td>
    <td align="right">20.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.90</td>
    <td align="right">21.44</td>
    <td align="right">16.35</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">32.31</td>
    <td align="right">35.85</td>
    <td align="right">24.90</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.64</td>
    <td align="right">33.33</td>
    <td align="right">24.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.28</td>
    <td align="right">3.91</td>
    <td align="right">3.94</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.66</td>
    <td align="right">5.88</td>
    <td align="right">5.88</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.00</td>
    <td align="right">6.06</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">9.41</td>
    <td align="right">9.13</td>
    <td align="right">9.15</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.89</td>
    <td align="right">9.84</td>
    <td align="right">9.89</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.43</td>
    <td align="right">11.95</td>
    <td align="right">11.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">17.27</td>
    <td align="right">20.67</td>
    <td align="right">14.80</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.51</td>
    <td align="right">26.41</td>
    <td align="right">21.91</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">25.81</td>
    <td align="right">26.20</td>
    <td align="right">21.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">19.96</td>
    <td align="right">23.67</td>
    <td align="right">16.52</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.76</td>
    <td align="right">36.98</td>
    <td align="right">25.30</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">32.63</td>
    <td align="right">36.83</td>
    <td align="right">25.14</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.18</td>
    <td align="right">5.96</td>
    <td align="right">4.29</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.58</td>
    <td align="right">10.60</td>
    <td align="right">17.12</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.58</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.11</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.75</td>
    <td align="right">15.46</td>
    <td align="right">18.54</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.14</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.67</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.81</td>
    <td align="right">18.62</td>
    <td align="right">17.12</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.65</td>
    <td align="right">5.06</td>
    <td align="right">5.07</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.01</td>
    <td align="right">5.96</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.89</td>
    <td align="right">23.23</td>
    <td align="right">17.97</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.29</td>
    <td align="right">3.50</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.69</td>
    <td align="right">11.29</td>
    <td align="right">17.68</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.82</td>
    <td align="right">4.31</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.23</td>
    <td align="right">4.89</td>
    <td align="right">4.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.35</td>
    <td align="right">16.28</td>
    <td align="right">19.08</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">5.24</td>
    <td align="right">4.74</td>
    <td align="right">4.75</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.82</td>
    <td align="right">5.59</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.28</td>
    <td align="right">20.14</td>
    <td align="right">17.64</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.84</td>
    <td align="right">5.18</td>
    <td align="right">5.18</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.14</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.09</td>
    <td align="right">24.59</td>
    <td align="right">18.04</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">6.12</td>
    <td align="right">5.81</td>
    <td align="right">5.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.47</td>
    <td align="right">3.72</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.33</td>
    <td align="right">3.90</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.41</td>
    <td align="right">3.75</td>
    <td align="right">3.76</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.80</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.00</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.01</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.30</td>
    <td align="right">2.31</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.01</td>
    <td align="right">6.48</td>
    <td align="right">6.49</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.19</td>
    <td align="right">6.49</td>
    <td align="right">6.60</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.42</td>
    <td align="right">4.35</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.53</td>
    <td align="right">7.50</td>
    <td align="right">7.32</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.03</td>
    <td align="right">7.74</td>
    <td align="right">7.60</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.46</td>
    <td align="right">4.38</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.45</td>
    <td align="right">4.16</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.54</td>
    <td align="right">3.99</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.06</td>
    <td align="right">2.82</td>
    <td align="right">2.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.92</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.18</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">3.25</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">6.31</td>
    <td align="right">7.17</td>
    <td align="right">7.18</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.50</td>
    <td align="right">6.82</td>
    <td align="right">6.67</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.69</td>
    <td align="right">4.72</td>
    <td align="right">3.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.59</td>
    <td align="right">7.52</td>
    <td align="right">7.52</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">7.12</td>
    <td align="right">7.87</td>
    <td align="right">7.68</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.74</td>
    <td align="right">4.75</td>
    <td align="right">3.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.84</td>
    <td align="right">2.38</td>
    <td align="right">2.38</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.88</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.96</td>
    <td align="right">3.96</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.90</td>
    <td align="right">2.42</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.23</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.13</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.51</td>
    <td align="right">4.31</td>
    <td align="right">3.04</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.87</td>
    <td align="right">6.32</td>
    <td align="right">4.68</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">6.08</td>
    <td align="right">6.12</td>
    <td align="right">4.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.58</td>
    <td align="right">4.33</td>
    <td align="right">3.03</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.03</td>
    <td align="right">7.00</td>
    <td align="right">4.54</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.28</td>
    <td align="right">6.97</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.02</td>
    <td align="right">2.66</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.06</td>
    <td align="right">4.45</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.12</td>
    <td align="right">2.72</td>
    <td align="right">2.71</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.97</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.36</td>
    <td align="right">4.28</td>
    <td align="right">4.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.77</td>
    <td align="right">4.58</td>
    <td align="right">3.29</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">6.29</td>
    <td align="right">6.70</td>
    <td align="right">5.30</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.43</td>
    <td align="right">6.19</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.82</td>
    <td align="right">4.61</td>
    <td align="right">3.30</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.27</td>
    <td align="right">7.55</td>
    <td align="right">5.33</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.56</td>
    <td align="right">7.28</td>
    <td align="right">5.20</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">50.67</td>
    <td align="right">23.81</td>
    <td align="right">14.53</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.30</td>
    <td align="right">14.28</td>
    <td align="right">19.75</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.78</td>
    <td align="right">5.36</td>
    <td align="right">5.38</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.95</td>
    <td align="right">7.76</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">44.06</td>
    <td align="right">43.57</td>
    <td align="right">25.45</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.32</td>
    <td align="right">11.16</td>
    <td align="right">11.13</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.54</td>
    <td align="right">12.86</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">72.05</td>
    <td align="right">79.87</td>
    <td align="right">31.51</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.13</td>
    <td align="right">17.44</td>
    <td align="right">17.45</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.89</td>
    <td align="right">20.55</td>
    <td align="right">20.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">104.17</td>
    <td align="right">104.50</td>
    <td align="right">35.55</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.42</td>
    <td align="right">21.62</td>
    <td align="right">21.61</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.46</td>
    <td align="right">15.17</td>
    <td align="right">15.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.21</td>
    <td align="right">14.03</td>
    <td align="right">20.06</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.09</td>
    <td align="right">5.57</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.82</td>
    <td align="right">5.56</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.34</td>
    <td align="right">46.70</td>
    <td align="right">25.85</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.93</td>
    <td align="right">11.02</td>
    <td align="right">11.02</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.83</td>
    <td align="right">13.05</td>
    <td align="right">13.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.15</td>
    <td align="right">85.92</td>
    <td align="right">31.40</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.91</td>
    <td align="right">18.09</td>
    <td align="right">18.06</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.24</td>
    <td align="right">21.12</td>
    <td align="right">21.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">123.13</td>
    <td align="right">119.78</td>
    <td align="right">36.62</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.42</td>
    <td align="right">21.75</td>
    <td align="right">21.74</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.83</td>
    <td align="right">16.76</td>
    <td align="right">16.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.44</td>
    <td align="right">6.12</td>
    <td align="right">6.18</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.64</td>
    <td align="right">5.25</td>
    <td align="right">5.25</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.45</td>
    <td align="right">3.27</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.64</td>
    <td align="right">8.85</td>
    <td align="right">8.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.55</td>
    <td align="right">10.98</td>
    <td align="right">11.00</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.96</td>
    <td align="right">7.26</td>
    <td align="right">7.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.95</td>
    <td align="right">20.77</td>
    <td align="right">20.79</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.90</td>
    <td align="right">21.60</td>
    <td align="right">21.62</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.69</td>
    <td align="right">15.98</td>
    <td align="right">11.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.25</td>
    <td align="right">26.89</td>
    <td align="right">26.90</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.68</td>
    <td align="right">30.42</td>
    <td align="right">30.42</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">17.02</td>
    <td align="right">18.16</td>
    <td align="right">13.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.28</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.33</td>
    <td align="right">4.91</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.55</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.51</td>
    <td align="right">9.65</td>
    <td align="right">9.70</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">10.31</td>
    <td align="right">11.75</td>
    <td align="right">11.76</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.73</td>
    <td align="right">7.56</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.80</td>
    <td align="right">21.66</td>
    <td align="right">21.69</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.99</td>
    <td align="right">21.48</td>
    <td align="right">21.46</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.32</td>
    <td align="right">17.36</td>
    <td align="right">12.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.95</td>
    <td align="right">26.92</td>
    <td align="right">26.92</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">26.76</td>
    <td align="right">30.76</td>
    <td align="right">30.77</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.94</td>
    <td align="right">19.87</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.44</td>
    <td align="right">3.09</td>
    <td align="right">3.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">7.30</td>
    <td align="right">8.11</td>
    <td align="right">8.23</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.15</td>
    <td align="right">5.41</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.60</td>
    <td align="right">7.67</td>
    <td align="right">7.63</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">7.62</td>
    <td align="right">8.75</td>
    <td align="right">8.78</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.25</td>
    <td align="right">10.52</td>
    <td align="right">10.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.90</td>
    <td align="right">16.16</td>
    <td align="right">11.71</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.45</td>
    <td align="right">21.01</td>
    <td align="right">16.64</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.85</td>
    <td align="right">21.27</td>
    <td align="right">16.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.26</td>
    <td align="right">18.26</td>
    <td align="right">13.16</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">24.80</td>
    <td align="right">26.74</td>
    <td align="right">19.35</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.19</td>
    <td align="right">26.84</td>
    <td align="right">19.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.81</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.80</td>
    <td align="right">6.41</td>
    <td align="right">6.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.89</td>
    <td align="right">7.44</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.02</td>
    <td align="right">7.96</td>
    <td align="right">7.96</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.84</td>
    <td align="right">9.88</td>
    <td align="right">9.89</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.77</td>
    <td align="right">11.08</td>
    <td align="right">11.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.80</td>
    <td align="right">17.78</td>
    <td align="right">12.93</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.12</td>
    <td align="right">21.52</td>
    <td align="right">17.96</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.27</td>
    <td align="right">21.59</td>
    <td align="right">16.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.93</td>
    <td align="right">19.94</td>
    <td align="right">14.41</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">27.92</td>
    <td align="right">29.92</td>
    <td align="right">21.57</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.25</td>
    <td align="right">30.04</td>
    <td align="right">19.65</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.54</td>
    <td align="right">2.55</td>
    <td align="right">2.02</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">6.30</td>
    <td align="right">4.42</td>
    <td align="right">11.37</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.31</td>
    <td align="right">1.18</td>
    <td align="right">1.17</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.61</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.46</td>
    <td align="right">6.63</td>
    <td align="right">11.77</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.37</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.69</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.41</td>
    <td align="right">8.18</td>
    <td align="right">11.04</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.73</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.58</td>
    <td align="right">10.74</td>
    <td align="right">11.24</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.73</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.33</td>
    <td align="right">4.14</td>
    <td align="right">11.38</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.29</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.61</td>
    <td align="right">1.27</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.42</td>
    <td align="right">6.06</td>
    <td align="right">11.96</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.72</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.64</td>
    <td align="right">7.34</td>
    <td align="right">11.15</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.60</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.96</td>
    <td align="right">9.35</td>
    <td align="right">11.42</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.24</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.27</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.01</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.18</td>
    <td align="right">1.93</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.81</td>
    <td align="right">2.20</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.50</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.07</td>
    <td align="right">2.87</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.10</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.96</td>
    <td align="right">2.40</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.58</td>
    <td align="right">3.69</td>
    <td align="right">3.70</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.81</td>
    <td align="right">4.38</td>
    <td align="right">4.39</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.01</td>
    <td align="right">2.93</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.29</td>
    <td align="right">1.73</td>
    <td align="right">1.71</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.30</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.00</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">1.93</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.73</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.41</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.10</td>
    <td align="right">2.90</td>
    <td align="right">2.94</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.07</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.89</td>
    <td align="right">2.41</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.61</td>
    <td align="right">3.75</td>
    <td align="right">3.75</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.78</td>
    <td align="right">4.32</td>
    <td align="right">4.31</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.91</td>
    <td align="right">2.93</td>
    <td align="right">1.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.02</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.24</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.26</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.05</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.16</td>
    <td align="right">1.92</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.82</td>
    <td align="right">2.21</td>
    <td align="right">2.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.85</td>
    <td align="right">2.36</td>
    <td align="right">1.73</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.09</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.08</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.87</td>
    <td align="right">2.86</td>
    <td align="right">1.71</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.58</td>
    <td align="right">3.74</td>
    <td align="right">3.66</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.73</td>
    <td align="right">4.32</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.01</td>
    <td align="right">1.67</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.33</td>
    <td align="right">1.75</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.03</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.20</td>
    <td align="right">1.93</td>
    <td align="right">1.94</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.84</td>
    <td align="right">2.26</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.88</td>
    <td align="right">2.38</td>
    <td align="right">1.75</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.16</td>
    <td align="right">2.96</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.12</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">1.77</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.70</td>
    <td align="right">3.69</td>
    <td align="right">3.67</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.71</td>
    <td align="right">4.38</td>
    <td align="right">4.38</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.86</td>
    <td align="right">11.11</td>
    <td align="right">5.85</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">7.75</td>
    <td align="right">6.23</td>
    <td align="right">12.86</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.00</td>
    <td align="right">1.96</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.12</td>
    <td align="right">2.05</td>
    <td align="right">2.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.31</td>
    <td align="right">11.32</td>
    <td align="right">16.11</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.86</td>
    <td align="right">3.80</td>
    <td align="right">3.66</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.33</td>
    <td align="right">3.27</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.72</td>
    <td align="right">25.62</td>
    <td align="right">18.26</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.35</td>
    <td align="right">6.41</td>
    <td align="right">6.46</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.74</td>
    <td align="right">6.34</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.88</td>
    <td align="right">39.89</td>
    <td align="right">20.50</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.94</td>
    <td align="right">7.75</td>
    <td align="right">7.76</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.56</td>
    <td align="right">6.71</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.73</td>
    <td align="right">6.15</td>
    <td align="right">12.95</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.08</td>
    <td align="right">2.00</td>
    <td align="right">2.00</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.12</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.78</td>
    <td align="right">12.03</td>
    <td align="right">16.35</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.57</td>
    <td align="right">3.81</td>
    <td align="right">3.50</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.16</td>
    <td align="right">3.14</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">28.67</td>
    <td align="right">23.71</td>
    <td align="right">18.21</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.89</td>
    <td align="right">6.58</td>
    <td align="right">6.34</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.99</td>
    <td align="right">6.38</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">52.48</td>
    <td align="right">40.50</td>
    <td align="right">20.75</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.12</td>
    <td align="right">8.04</td>
    <td align="right">8.17</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.84</td>
    <td align="right">6.43</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.71</td>
    <td align="right">2.57</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.75</td>
    <td align="right">2.65</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.44</td>
    <td align="right">2.57</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.41</td>
    <td align="right">5.06</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.26</td>
    <td align="right">5.21</td>
    <td align="right">4.90</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.06</td>
    <td align="right">3.77</td>
    <td align="right">3.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.26</td>
    <td align="right">9.79</td>
    <td align="right">9.61</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.30</td>
    <td align="right">9.18</td>
    <td align="right">8.61</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.25</td>
    <td align="right">7.36</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.41</td>
    <td align="right">14.59</td>
    <td align="right">14.64</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.49</td>
    <td align="right">16.61</td>
    <td align="right">16.75</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.50</td>
    <td align="right">11.22</td>
    <td align="right">6.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.74</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.40</td>
    <td align="right">2.56</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.93</td>
    <td align="right">4.24</td>
    <td align="right">4.26</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.28</td>
    <td align="right">4.87</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">3.17</td>
    <td align="right">3.61</td>
    <td align="right">3.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.45</td>
    <td align="right">9.82</td>
    <td align="right">9.75</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.39</td>
    <td align="right">9.30</td>
    <td align="right">9.52</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.35</td>
    <td align="right">8.15</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.45</td>
    <td align="right">14.17</td>
    <td align="right">14.33</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.87</td>
    <td align="right">15.96</td>
    <td align="right">17.37</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.52</td>
    <td align="right">11.02</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.40</td>
    <td align="right">2.54</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.73</td>
    <td align="right">2.55</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.74</td>
    <td align="right">2.62</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.13</td>
    <td align="right">3.47</td>
    <td align="right">3.33</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.29</td>
    <td align="right">4.46</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.75</td>
    <td align="right">5.14</td>
    <td align="right">4.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.21</td>
    <td align="right">8.12</td>
    <td align="right">5.71</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.33</td>
    <td align="right">9.95</td>
    <td align="right">9.51</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.52</td>
    <td align="right">9.52</td>
    <td align="right">9.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.88</td>
    <td align="right">11.44</td>
    <td align="right">6.39</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.19</td>
    <td align="right">15.01</td>
    <td align="right">14.81</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.74</td>
    <td align="right">16.09</td>
    <td align="right">15.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.36</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.69</td>
    <td align="right">2.51</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.70</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.81</td>
    <td align="right">2.97</td>
    <td align="right">3.03</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.71</td>
    <td align="right">4.09</td>
    <td align="right">4.08</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.17</td>
    <td align="right">4.86</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.15</td>
    <td align="right">7.31</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.61</td>
    <td align="right">8.79</td>
    <td align="right">8.75</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.60</td>
    <td align="right">8.60</td>
    <td align="right">8.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.43</td>
    <td align="right">10.25</td>
    <td align="right">5.97</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.11</td>
    <td align="right">13.12</td>
    <td align="right">13.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.61</td>
    <td align="right">15.22</td>
    <td align="right">15.23</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.99</td>
    <td align="right">5.28</td>
    <td align="right">3.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.23</td>
    <td align="right">10.49</td>
    <td align="right">13.88</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.70</td>
    <td align="right">3.44</td>
    <td align="right">3.46</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.28</td>
    <td align="right">4.09</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.58</td>
    <td align="right">14.89</td>
    <td align="right">15.09</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.33</td>
    <td align="right">3.88</td>
    <td align="right">3.84</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.94</td>
    <td align="right">4.73</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.32</td>
    <td align="right">18.22</td>
    <td align="right">13.88</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.01</td>
    <td align="right">4.28</td>
    <td align="right">4.25</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.58</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.44</td>
    <td align="right">23.08</td>
    <td align="right">14.49</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.67</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.17</td>
    <td align="right">5.55</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.30</td>
    <td align="right">11.33</td>
    <td align="right">14.41</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.61</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.38</td>
    <td align="right">4.16</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.12</td>
    <td align="right">16.28</td>
    <td align="right">15.14</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.44</td>
    <td align="right">4.02</td>
    <td align="right">3.99</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.05</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.29</td>
    <td align="right">20.34</td>
    <td align="right">13.93</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.10</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">5.14</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.95</td>
    <td align="right">99.58</td>
    <td align="right">25.27</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.94</td>
    <td align="right">4.74</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.33</td>
    <td align="right">5.60</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.29</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">8.41</td>
    <td align="right">4.58</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.24</td>
    <td align="right">7.13</td>
    <td align="right">7.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.92</td>
    <td align="right">6.84</td>
    <td align="right">6.74</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.80</td>
    <td align="right">2.88</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.57</td>
    <td align="right">10.12</td>
    <td align="right">10.04</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.36</td>
    <td align="right">10.60</td>
    <td align="right">10.57</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.59</td>
    <td align="right">4.41</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.65</td>
    <td align="right">11.13</td>
    <td align="right">11.04</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.34</td>
    <td align="right">25.39</td>
    <td align="right">25.46</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.32</td>
    <td align="right">4.42</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.40</td>
    <td align="right">4.41</td>
    <td align="right">4.41</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.37</td>
    <td align="right">4.70</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.86</td>
    <td align="right">2.19</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.29</td>
    <td align="right">7.17</td>
    <td align="right">7.10</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.70</td>
    <td align="right">7.08</td>
    <td align="right">7.06</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.75</td>
    <td align="right">2.99</td>
    <td align="right">2.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.56</td>
    <td align="right">10.17</td>
    <td align="right">10.14</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.28</td>
    <td align="right">10.63</td>
    <td align="right">10.64</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.29</td>
    <td align="right">4.46</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">13.49</td>
    <td align="right">11.17</td>
    <td align="right">11.13</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.84</td>
    <td align="right">12.53</td>
    <td align="right">12.52</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.03</td>
    <td align="right">4.44</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.82</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.71</td>
    <td align="right">3.19</td>
    <td align="right">3.20</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.77</td>
    <td align="right">2.99</td>
    <td align="right">3.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.23</td>
    <td align="right">3.27</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.19</td>
    <td align="right">3.80</td>
    <td align="right">3.22</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">5.98</td>
    <td align="right">4.50</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.41</td>
    <td align="right">4.18</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.84</td>
    <td align="right">6.36</td>
    <td align="right">4.84</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.49</td>
    <td align="right">6.15</td>
    <td align="right">4.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.43</td>
    <td align="right">4.25</td>
    <td align="right">2.89</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.10</td>
    <td align="right">6.88</td>
    <td align="right">4.88</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.78</td>
    <td align="right">6.73</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.82</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.78</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">3.38</td>
    <td align="right">2.73</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.17</td>
    <td align="right">3.90</td>
    <td align="right">3.26</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.71</td>
    <td align="right">4.57</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.36</td>
    <td align="right">4.32</td>
    <td align="right">2.98</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.03</td>
    <td align="right">6.45</td>
    <td align="right">5.02</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.70</td>
    <td align="right">6.30</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.26</td>
    <td align="right">4.34</td>
    <td align="right">2.99</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.88</td>
    <td align="right">7.04</td>
    <td align="right">5.07</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.96</td>
    <td align="right">6.87</td>
    <td align="right">5.14</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.79</td>
    <td align="right">23.54</td>
    <td align="right">13.96</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.00</td>
    <td align="right">11.09</td>
    <td align="right">15.33</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.03</td>
    <td align="right">3.66</td>
    <td align="right">3.77</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.60</td>
    <td align="right">4.37</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.39</td>
    <td align="right">18.88</td>
    <td align="right">16.55</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.18</td>
    <td align="right">12.30</td>
    <td align="right">12.26</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.99</td>
    <td align="right">6.64</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">65.53</td>
    <td align="right">74.13</td>
    <td align="right">24.74</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.18</td>
    <td align="right">13.25</td>
    <td align="right">13.29</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.15</td>
    <td align="right">15.74</td>
    <td align="right">15.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.33</td>
    <td align="right">109.56</td>
    <td align="right">29.54</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.45</td>
    <td align="right">16.69</td>
    <td align="right">16.47</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.43</td>
    <td align="right">22.57</td>
    <td align="right">22.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.00</td>
    <td align="right">11.83</td>
    <td align="right">15.81</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.16</td>
    <td align="right">3.78</td>
    <td align="right">3.81</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.69</td>
    <td align="right">4.51</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">23.87</td>
    <td align="right">18.76</td>
    <td align="right">16.82</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.20</td>
    <td align="right">5.76</td>
    <td align="right">5.77</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.08</td>
    <td align="right">6.64</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">70.10</td>
    <td align="right">79.81</td>
    <td align="right">26.02</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.55</td>
    <td align="right">13.62</td>
    <td align="right">13.63</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.48</td>
    <td align="right">15.85</td>
    <td align="right">15.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.51</td>
    <td align="right">117.44</td>
    <td align="right">31.16</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.67</td>
    <td align="right">18.26</td>
    <td align="right">18.18</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.74</td>
    <td align="right">22.57</td>
    <td align="right">22.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.96</td>
    <td align="right">4.65</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.05</td>
    <td align="right">4.93</td>
    <td align="right">4.96</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.10</td>
    <td align="right">2.24</td>
    <td align="right">2.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.22</td>
    <td align="right">18.74</td>
    <td align="right">18.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.22</td>
    <td align="right">9.61</td>
    <td align="right">9.62</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.81</td>
    <td align="right">8.94</td>
    <td align="right">7.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">26.14</td>
    <td align="right">25.89</td>
    <td align="right">25.79</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">29.95</td>
    <td align="right">28.57</td>
    <td align="right">28.57</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.12</td>
    <td align="right">15.44</td>
    <td align="right">10.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">35.78</td>
    <td align="right">35.71</td>
    <td align="right">35.98</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">39.82</td>
    <td align="right">38.03</td>
    <td align="right">37.94</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.29</td>
    <td align="right">17.82</td>
    <td align="right">12.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.06</td>
    <td align="right">4.72</td>
    <td align="right">4.79</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.65</td>
    <td align="right">5.02</td>
    <td align="right">5.09</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.12</td>
    <td align="right">2.32</td>
    <td align="right">2.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.25</td>
    <td align="right">9.20</td>
    <td align="right">9.04</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.95</td>
    <td align="right">9.57</td>
    <td align="right">9.33</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.87</td>
    <td align="right">7.16</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.64</td>
    <td align="right">26.05</td>
    <td align="right">26.06</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.78</td>
    <td align="right">28.14</td>
    <td align="right">27.94</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.12</td>
    <td align="right">15.43</td>
    <td align="right">10.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.89</td>
    <td align="right">35.54</td>
    <td align="right">35.73</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">38.64</td>
    <td align="right">37.25</td>
    <td align="right">37.23</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.36</td>
    <td align="right">17.86</td>
    <td align="right">12.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.13</td>
    <td align="right">2.03</td>
    <td align="right">2.10</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.10</td>
    <td align="right">3.43</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.14</td>
    <td align="right">3.15</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.24</td>
    <td align="right">5.14</td>
    <td align="right">4.41</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.14</td>
    <td align="right">5.72</td>
    <td align="right">5.08</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">8.05</td>
    <td align="right">6.25</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.36</td>
    <td align="right">15.42</td>
    <td align="right">10.87</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.16</td>
    <td align="right">19.09</td>
    <td align="right">15.95</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.60</td>
    <td align="right">19.01</td>
    <td align="right">16.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.84</td>
    <td align="right">17.81</td>
    <td align="right">12.22</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.42</td>
    <td align="right">26.59</td>
    <td align="right">18.79</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.10</td>
    <td align="right">23.99</td>
    <td align="right">18.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.08</td>
    <td align="right">2.17</td>
    <td align="right">2.24</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.05</td>
    <td align="right">3.45</td>
    <td align="right">3.49</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.14</td>
    <td align="right">3.33</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.24</td>
    <td align="right">5.46</td>
    <td align="right">4.54</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.06</td>
    <td align="right">5.63</td>
    <td align="right">4.91</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.68</td>
    <td align="right">6.71</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.35</td>
    <td align="right">15.42</td>
    <td align="right">10.92</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.11</td>
    <td align="right">19.11</td>
    <td align="right">16.13</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.07</td>
    <td align="right">19.69</td>
    <td align="right">16.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.77</td>
    <td align="right">17.73</td>
    <td align="right">12.33</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.63</td>
    <td align="right">26.93</td>
    <td align="right">18.99</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.73</td>
    <td align="right">26.93</td>
    <td align="right">19.03</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.63</td>
    <td align="right">37.11</td>
    <td align="right">14.40</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.93</td>
    <td align="right">44.73</td>
    <td align="right">37.79</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.31</td>
    <td align="right">18.26</td>
    <td align="right">18.25</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.14</td>
    <td align="right">20.00</td>
    <td align="right">20.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.71</td>
    <td align="right">67.78</td>
    <td align="right">40.36</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.19</td>
    <td align="right">21.30</td>
    <td align="right">21.46</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">15.99</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">51.06</td>
    <td align="right">83.90</td>
    <td align="right">39.08</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.56</td>
    <td align="right">19.64</td>
    <td align="right">19.10</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.39</td>
    <td align="right">21.10</td>
    <td align="right">21.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.81</td>
    <td align="right">104.95</td>
    <td align="right">39.70</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.59</td>
    <td align="right">20.60</td>
    <td align="right">20.61</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.43</td>
    <td align="right">22.02</td>
    <td align="right">22.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.93</td>
    <td align="right">44.23</td>
    <td align="right">37.63</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.37</td>
    <td align="right">16.27</td>
    <td align="right">16.16</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.65</td>
    <td align="right">17.49</td>
    <td align="right">17.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.78</td>
    <td align="right">67.37</td>
    <td align="right">40.48</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.52</td>
    <td align="right">18.22</td>
    <td align="right">18.46</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.12</td>
    <td align="right">19.04</td>
    <td align="right">19.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.28</td>
    <td align="right">82.21</td>
    <td align="right">39.07</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.46</td>
    <td align="right">20.48</td>
    <td align="right">20.49</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.09</td>
    <td align="right">21.03</td>
    <td align="right">21.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.95</td>
    <td align="right">100.23</td>
    <td align="right">40.73</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">22.20</td>
    <td align="right">22.20</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.91</td>
    <td align="right">23.16</td>
    <td align="right">22.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.45</td>
    <td align="right">22.07</td>
    <td align="right">22.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.62</td>
    <td align="right">25.60</td>
    <td align="right">25.58</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.12</td>
    <td align="right">15.57</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.88</td>
    <td align="right">29.63</td>
    <td align="right">29.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.27</td>
    <td align="right">32.53</td>
    <td align="right">32.55</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.17</td>
    <td align="right">17.83</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.86</td>
    <td align="right">36.08</td>
    <td align="right">35.41</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.42</td>
    <td align="right">48.11</td>
    <td align="right">48.20</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.38</td>
    <td align="right">20.83</td>
    <td align="right">20.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.63</td>
    <td align="right">39.86</td>
    <td align="right">39.86</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.87</td>
    <td align="right">56.29</td>
    <td align="right">56.65</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.73</td>
    <td align="right">25.05</td>
    <td align="right">25.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.93</td>
    <td align="right">22.83</td>
    <td align="right">22.76</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">26.53</td>
    <td align="right">26.42</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.28</td>
    <td align="right">15.94</td>
    <td align="right">15.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.51</td>
    <td align="right">30.16</td>
    <td align="right">30.25</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.02</td>
    <td align="right">34.61</td>
    <td align="right">34.60</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.83</td>
    <td align="right">18.33</td>
    <td align="right">18.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.34</td>
    <td align="right">36.69</td>
    <td align="right">36.73</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.69</td>
    <td align="right">48.12</td>
    <td align="right">48.15</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">16.84</td>
    <td align="right">20.84</td>
    <td align="right">20.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">41.88</td>
    <td align="right">41.83</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.58</td>
    <td align="right">56.51</td>
    <td align="right">56.59</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.76</td>
    <td align="right">25.83</td>
    <td align="right">25.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.12</td>
    <td align="right">15.47</td>
    <td align="right">15.95</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.48</td>
    <td align="right">22.07</td>
    <td align="right">22.06</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.63</td>
    <td align="right">25.58</td>
    <td align="right">25.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">18.91</td>
    <td align="right">19.28</td>
    <td align="right">19.33</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.07</td>
    <td align="right">29.66</td>
    <td align="right">29.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.22</td>
    <td align="right">32.49</td>
    <td align="right">32.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">23.70</td>
    <td align="right">23.54</td>
    <td align="right">23.54</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.00</td>
    <td align="right">35.43</td>
    <td align="right">35.42</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.44</td>
    <td align="right">48.09</td>
    <td align="right">48.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">30.86</td>
    <td align="right">32.11</td>
    <td align="right">32.04</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.19</td>
    <td align="right">39.80</td>
    <td align="right">39.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.98</td>
    <td align="right">56.32</td>
    <td align="right">56.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.03</td>
    <td align="right">16.98</td>
    <td align="right">16.91</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.91</td>
    <td align="right">22.77</td>
    <td align="right">22.75</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.64</td>
    <td align="right">26.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.27</td>
    <td align="right">20.43</td>
    <td align="right">20.45</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.57</td>
    <td align="right">30.24</td>
    <td align="right">30.16</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.55</td>
    <td align="right">34.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">22.53</td>
    <td align="right">24.03</td>
    <td align="right">24.27</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.21</td>
    <td align="right">36.79</td>
    <td align="right">36.76</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.78</td>
    <td align="right">48.03</td>
    <td align="right">48.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">30.92</td>
    <td align="right">34.48</td>
    <td align="right">34.47</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.20</td>
    <td align="right">41.80</td>
    <td align="right">41.75</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.55</td>
    <td align="right">56.60</td>
    <td align="right">56.66</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">107.66</td>
    <td align="right">126.28</td>
    <td align="right">26.95</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">34.40</td>
    <td align="right">53.86</td>
    <td align="right">45.56</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">18.02</td>
    <td align="right">23.59</td>
    <td align="right">23.58</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">19.56</td>
    <td align="right">24.34</td>
    <td align="right">25.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">90.04</td>
    <td align="right">129.24</td>
    <td align="right">60.63</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.09</td>
    <td align="right">33.69</td>
    <td align="right">33.73</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.72</td>
    <td align="right">33.31</td>
    <td align="right">34.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">174.07</td>
    <td align="right">253.48</td>
    <td align="right">78.19</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.23</td>
    <td align="right">46.45</td>
    <td align="right">48.04</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.45</td>
    <td align="right">48.38</td>
    <td align="right">48.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">267.79</td>
    <td align="right">403.41</td>
    <td align="right">97.68</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">46.92</td>
    <td align="right">59.73</td>
    <td align="right">59.75</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">60.14</td>
    <td align="right">64.71</td>
    <td align="right">64.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">33.17</td>
    <td align="right">47.98</td>
    <td align="right">42.76</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.28</td>
    <td align="right">18.12</td>
    <td align="right">18.00</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.00</td>
    <td align="right">19.89</td>
    <td align="right">19.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">98.56</td>
    <td align="right">130.07</td>
    <td align="right">60.56</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.22</td>
    <td align="right">27.15</td>
    <td align="right">27.67</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.49</td>
    <td align="right">32.45</td>
    <td align="right">32.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.24</td>
    <td align="right">246.62</td>
    <td align="right">79.51</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.53</td>
    <td align="right">46.85</td>
    <td align="right">46.86</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.31</td>
    <td align="right">49.94</td>
    <td align="right">50.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">298.41</td>
    <td align="right">402.55</td>
    <td align="right">98.51</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.83</td>
    <td align="right">61.88</td>
    <td align="right">62.09</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">51.03</td>
    <td align="right">63.18</td>
    <td align="right">63.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">21.34</td>
    <td align="right">24.26</td>
    <td align="right">24.31</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.49</td>
    <td align="right">31.72</td>
    <td align="right">31.69</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">14.85</td>
    <td align="right">19.48</td>
    <td align="right">18.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">37.70</td>
    <td align="right">43.06</td>
    <td align="right">42.99</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">54.47</td>
    <td align="right">52.28</td>
    <td align="right">50.74</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">23.50</td>
    <td align="right">27.35</td>
    <td align="right">27.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.87</td>
    <td align="right">69.34</td>
    <td align="right">68.28</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.68</td>
    <td align="right">80.32</td>
    <td align="right">81.37</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">41.72</td>
    <td align="right">45.16</td>
    <td align="right">45.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.40</td>
    <td align="right">90.60</td>
    <td align="right">90.74</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.59</td>
    <td align="right">107.36</td>
    <td align="right">107.60</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">69.56</td>
    <td align="right">73.91</td>
    <td align="right">74.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">25.12</td>
    <td align="right">27.97</td>
    <td align="right">27.97</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.07</td>
    <td align="right">31.47</td>
    <td align="right">31.43</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.51</td>
    <td align="right">19.20</td>
    <td align="right">18.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.20</td>
    <td align="right">45.06</td>
    <td align="right">44.90</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">51.98</td>
    <td align="right">52.72</td>
    <td align="right">52.60</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.86</td>
    <td align="right">29.63</td>
    <td align="right">29.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.54</td>
    <td align="right">71.03</td>
    <td align="right">71.32</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.23</td>
    <td align="right">83.25</td>
    <td align="right">83.30</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">41.85</td>
    <td align="right">45.48</td>
    <td align="right">45.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.55</td>
    <td align="right">94.41</td>
    <td align="right">96.84</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.53</td>
    <td align="right">108.71</td>
    <td align="right">108.83</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.79</td>
    <td align="right">78.20</td>
    <td align="right">78.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.84</td>
    <td align="right">18.79</td>
    <td align="right">18.44</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.41</td>
    <td align="right">25.26</td>
    <td align="right">25.30</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">28.52</td>
    <td align="right">29.66</td>
    <td align="right">31.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">29.78</td>
    <td align="right">30.89</td>
    <td align="right">30.33</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">41.54</td>
    <td align="right">41.01</td>
    <td align="right">40.96</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">55.65</td>
    <td align="right">50.20</td>
    <td align="right">48.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">47.79</td>
    <td align="right">48.17</td>
    <td align="right">48.22</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.29</td>
    <td align="right">68.11</td>
    <td align="right">68.47</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">102.23</td>
    <td align="right">82.02</td>
    <td align="right">82.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">80.70</td>
    <td align="right">85.47</td>
    <td align="right">84.61</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.45</td>
    <td align="right">92.67</td>
    <td align="right">92.84</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.98</td>
    <td align="right">108.18</td>
    <td align="right">108.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">18.07</td>
    <td align="right">22.68</td>
    <td align="right">22.23</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.79</td>
    <td align="right">26.78</td>
    <td align="right">26.85</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.71</td>
    <td align="right">32.07</td>
    <td align="right">32.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">31.51</td>
    <td align="right">31.21</td>
    <td align="right">31.20</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.60</td>
    <td align="right">46.43</td>
    <td align="right">46.33</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">52.72</td>
    <td align="right">51.51</td>
    <td align="right">51.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">47.05</td>
    <td align="right">48.15</td>
    <td align="right">48.22</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.61</td>
    <td align="right">71.70</td>
    <td align="right">71.60</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.87</td>
    <td align="right">82.78</td>
    <td align="right">82.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.96</td>
    <td align="right">87.47</td>
    <td align="right">87.40</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.16</td>
    <td align="right">92.56</td>
    <td align="right">92.39</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.76</td>
    <td align="right">108.24</td>
    <td align="right">108.29</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.55</td>
    <td align="right">13.93</td>
    <td align="right">8.53</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">15.87</td>
    <td align="right">22.93</td>
    <td align="right">26.66</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.07</td>
    <td align="right">13.43</td>
    <td align="right">13.43</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.80</td>
    <td align="right">16.23</td>
    <td align="right">16.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.16</td>
    <td align="right">33.61</td>
    <td align="right">29.02</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.31</td>
    <td align="right">16.52</td>
    <td align="right">16.66</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.11</td>
    <td align="right">18.74</td>
    <td align="right">18.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.99</td>
    <td align="right">43.33</td>
    <td align="right">29.12</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.62</td>
    <td align="right">19.10</td>
    <td align="right">19.10</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.69</td>
    <td align="right">22.02</td>
    <td align="right">22.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.62</td>
    <td align="right">53.01</td>
    <td align="right">30.01</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.07</td>
    <td align="right">22.03</td>
    <td align="right">22.42</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.26</td>
    <td align="right">24.38</td>
    <td align="right">24.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.62</td>
    <td align="right">28.36</td>
    <td align="right">29.23</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">13.91</td>
    <td align="right">14.03</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.84</td>
    <td align="right">18.00</td>
    <td align="right">17.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.89</td>
    <td align="right">43.04</td>
    <td align="right">31.27</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.03</td>
    <td align="right">18.39</td>
    <td align="right">18.44</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.22</td>
    <td align="right">20.78</td>
    <td align="right">20.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.33</td>
    <td align="right">67.65</td>
    <td align="right">32.26</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.52</td>
    <td align="right">20.93</td>
    <td align="right">21.12</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.01</td>
    <td align="right">22.86</td>
    <td align="right">22.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.06</td>
    <td align="right">78.85</td>
    <td align="right">33.25</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.20</td>
    <td align="right">23.21</td>
    <td align="right">23.29</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.04</td>
    <td align="right">25.71</td>
    <td align="right">25.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.26</td>
    <td align="right">17.00</td>
    <td align="right">17.14</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">15.98</td>
    <td align="right">17.08</td>
    <td align="right">17.10</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.82</td>
    <td align="right">8.69</td>
    <td align="right">8.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.94</td>
    <td align="right">25.87</td>
    <td align="right">26.05</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.24</td>
    <td align="right">26.10</td>
    <td align="right">26.11</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.07</td>
    <td align="right">12.54</td>
    <td align="right">12.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.28</td>
    <td align="right">36.36</td>
    <td align="right">36.36</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.35</td>
    <td align="right">35.68</td>
    <td align="right">35.77</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.57</td>
    <td align="right">15.41</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.43</td>
    <td align="right">38.82</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.59</td>
    <td align="right">40.50</td>
    <td align="right">40.66</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.66</td>
    <td align="right">20.28</td>
    <td align="right">20.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.06</td>
    <td align="right">18.34</td>
    <td align="right">18.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.13</td>
    <td align="right">18.88</td>
    <td align="right">18.89</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.99</td>
    <td align="right">8.72</td>
    <td align="right">8.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.73</td>
    <td align="right">26.56</td>
    <td align="right">26.60</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.57</td>
    <td align="right">26.95</td>
    <td align="right">26.93</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.77</td>
    <td align="right">13.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.15</td>
    <td align="right">35.41</td>
    <td align="right">35.27</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">34.14</td>
    <td align="right">34.22</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.86</td>
    <td align="right">17.83</td>
    <td align="right">17.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.24</td>
    <td align="right">38.25</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.44</td>
    <td align="right">41.08</td>
    <td align="right">41.13</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.11</td>
    <td align="right">19.73</td>
    <td align="right">19.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">7.27</td>
    <td align="right">8.51</td>
    <td align="right">8.81</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.29</td>
    <td align="right">17.04</td>
    <td align="right">17.18</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.17</td>
    <td align="right">17.19</td>
    <td align="right">17.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.98</td>
    <td align="right">12.19</td>
    <td align="right">12.19</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.94</td>
    <td align="right">25.86</td>
    <td align="right">26.04</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.25</td>
    <td align="right">26.06</td>
    <td align="right">26.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.03</td>
    <td align="right">15.29</td>
    <td align="right">15.20</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.31</td>
    <td align="right">36.42</td>
    <td align="right">36.40</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.35</td>
    <td align="right">35.75</td>
    <td align="right">35.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.56</td>
    <td align="right">19.06</td>
    <td align="right">19.07</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.44</td>
    <td align="right">38.82</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.58</td>
    <td align="right">40.54</td>
    <td align="right">40.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.66</td>
    <td align="right">8.65</td>
    <td align="right">8.58</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">18.45</td>
    <td align="right">18.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.05</td>
    <td align="right">18.84</td>
    <td align="right">18.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.92</td>
    <td align="right">14.10</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.70</td>
    <td align="right">26.57</td>
    <td align="right">26.61</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">26.95</td>
    <td align="right">26.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.24</td>
    <td align="right">17.22</td>
    <td align="right">17.22</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.16</td>
    <td align="right">35.33</td>
    <td align="right">35.34</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.55</td>
    <td align="right">34.12</td>
    <td align="right">34.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">19.99</td>
    <td align="right">20.00</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.25</td>
    <td align="right">38.27</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.48</td>
    <td align="right">41.11</td>
    <td align="right">41.07</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.58</td>
    <td align="right">62.12</td>
    <td align="right">23.43</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">19.67</td>
    <td align="right">28.63</td>
    <td align="right">31.39</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">14.33</td>
    <td align="right">16.07</td>
    <td align="right">15.82</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.35</td>
    <td align="right">18.61</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">63.17</td>
    <td align="right">84.51</td>
    <td align="right">43.74</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.19</td>
    <td align="right">26.49</td>
    <td align="right">26.58</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.03</td>
    <td align="right">30.97</td>
    <td align="right">30.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">114.42</td>
    <td align="right">158.26</td>
    <td align="right">58.49</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.31</td>
    <td align="right">46.30</td>
    <td align="right">46.24</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">48.99</td>
    <td align="right">50.30</td>
    <td align="right">50.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">163.93</td>
    <td align="right">243.00</td>
    <td align="right">71.49</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.55</td>
    <td align="right">61.70</td>
    <td align="right">61.60</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">66.79</td>
    <td align="right">67.48</td>
    <td align="right">67.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">27.19</td>
    <td align="right">34.77</td>
    <td align="right">34.42</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.63</td>
    <td align="right">16.18</td>
    <td align="right">16.17</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.28</td>
    <td align="right">20.49</td>
    <td align="right">20.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">81.63</td>
    <td align="right">100.51</td>
    <td align="right">47.85</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.68</td>
    <td align="right">27.56</td>
    <td align="right">27.48</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.19</td>
    <td align="right">34.87</td>
    <td align="right">34.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">145.25</td>
    <td align="right">207.51</td>
    <td align="right">67.70</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">42.21</td>
    <td align="right">50.76</td>
    <td align="right">50.56</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.29</td>
    <td align="right">49.88</td>
    <td align="right">49.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">250.30</td>
    <td align="right">316.12</td>
    <td align="right">82.75</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">65.12</td>
    <td align="right">65.61</td>
    <td align="right">65.62</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.84</td>
    <td align="right">69.29</td>
    <td align="right">69.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.01</td>
    <td align="right">21.64</td>
    <td align="right">21.63</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.69</td>
    <td align="right">21.13</td>
    <td align="right">21.17</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">9.44</td>
    <td align="right">10.63</td>
    <td align="right">10.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">33.14</td>
    <td align="right">38.41</td>
    <td align="right">38.81</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.26</td>
    <td align="right">42.75</td>
    <td align="right">42.89</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">20.14</td>
    <td align="right">21.31</td>
    <td align="right">21.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">69.34</td>
    <td align="right">70.70</td>
    <td align="right">70.77</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.19</td>
    <td align="right">69.51</td>
    <td align="right">69.39</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.91</td>
    <td align="right">38.66</td>
    <td align="right">38.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.71</td>
    <td align="right">86.46</td>
    <td align="right">86.39</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.35</td>
    <td align="right">93.51</td>
    <td align="right">95.16</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">51.72</td>
    <td align="right">51.88</td>
    <td align="right">51.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.80</td>
    <td align="right">21.46</td>
    <td align="right">21.55</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.29</td>
    <td align="right">21.37</td>
    <td align="right">21.34</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.85</td>
    <td align="right">10.77</td>
    <td align="right">10.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.20</td>
    <td align="right">38.81</td>
    <td align="right">39.00</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">40.20</td>
    <td align="right">42.30</td>
    <td align="right">42.20</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.69</td>
    <td align="right">23.88</td>
    <td align="right">24.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.32</td>
    <td align="right">68.83</td>
    <td align="right">68.96</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.37</td>
    <td align="right">67.87</td>
    <td align="right">67.96</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.69</td>
    <td align="right">40.63</td>
    <td align="right">40.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.12</td>
    <td align="right">88.59</td>
    <td align="right">88.60</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.79</td>
    <td align="right">91.75</td>
    <td align="right">92.85</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.06</td>
    <td align="right">51.48</td>
    <td align="right">51.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">8.20</td>
    <td align="right">9.30</td>
    <td align="right">9.32</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">19.61</td>
    <td align="right">19.58</td>
    <td align="right">19.54</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.54</td>
    <td align="right">21.03</td>
    <td align="right">21.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">21.18</td>
    <td align="right">23.37</td>
    <td align="right">22.80</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.15</td>
    <td align="right">40.25</td>
    <td align="right">40.74</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.25</td>
    <td align="right">43.26</td>
    <td align="right">43.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">35.62</td>
    <td align="right">39.50</td>
    <td align="right">37.65</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.44</td>
    <td align="right">69.97</td>
    <td align="right">69.94</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.33</td>
    <td align="right">71.12</td>
    <td align="right">71.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.90</td>
    <td align="right">52.25</td>
    <td align="right">52.09</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">88.27</td>
    <td align="right">87.66</td>
    <td align="right">87.63</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.06</td>
    <td align="right">91.90</td>
    <td align="right">93.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.70</td>
    <td align="right">11.15</td>
    <td align="right">11.14</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.34</td>
    <td align="right">21.87</td>
    <td align="right">21.91</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.37</td>
    <td align="right">23.22</td>
    <td align="right">23.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.61</td>
    <td align="right">26.36</td>
    <td align="right">25.48</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.01</td>
    <td align="right">38.05</td>
    <td align="right">38.24</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.42</td>
    <td align="right">44.06</td>
    <td align="right">43.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.53</td>
    <td align="right">39.76</td>
    <td align="right">39.77</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.94</td>
    <td align="right">69.24</td>
    <td align="right">69.20</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.45</td>
    <td align="right">66.69</td>
    <td align="right">66.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.37</td>
    <td align="right">54.10</td>
    <td align="right">54.03</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.21</td>
    <td align="right">88.66</td>
    <td align="right">88.70</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.16</td>
    <td align="right">91.04</td>
    <td align="right">92.11</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.01</td>
    <td align="right">6.69</td>
    <td align="right">5.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">50.53</td>
    <td align="right">46.03</td>
    <td align="right">32.29</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.32</td>
    <td align="right">18.58</td>
    <td align="right">21.72</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.75</td>
    <td align="right">22.42</td>
    <td align="right">24.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">74.69</td>
    <td align="right">65.32</td>
    <td align="right">34.22</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.89</td>
    <td align="right">19.82</td>
    <td align="right">21.78</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.22</td>
    <td align="right">25.31</td>
    <td align="right">27.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">94.14</td>
    <td align="right">80.92</td>
    <td align="right">33.47</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.13</td>
    <td align="right">23.11</td>
    <td align="right">24.36</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.66</td>
    <td align="right">27.28</td>
    <td align="right">28.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">117.08</td>
    <td align="right">100.24</td>
    <td align="right">34.45</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.32</td>
    <td align="right">24.54</td>
    <td align="right">25.36</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.01</td>
    <td align="right">29.16</td>
    <td align="right">29.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.59</td>
    <td align="right">61.13</td>
    <td align="right">40.94</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.97</td>
    <td align="right">20.72</td>
    <td align="right">23.22</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.82</td>
    <td align="right">25.38</td>
    <td align="right">26.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">101.39</td>
    <td align="right">87.37</td>
    <td align="right">42.49</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.28</td>
    <td align="right">22.17</td>
    <td align="right">23.24</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.70</td>
    <td align="right">28.06</td>
    <td align="right">28.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.57</td>
    <td align="right">105.60</td>
    <td align="right">40.88</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.28</td>
    <td align="right">25.39</td>
    <td align="right">25.98</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.37</td>
    <td align="right">30.19</td>
    <td align="right">30.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.91</td>
    <td align="right">135.91</td>
    <td align="right">41.92</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.71</td>
    <td align="right">29.34</td>
    <td align="right">29.71</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.36</td>
    <td align="right">37.98</td>
    <td align="right">37.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">21.21</td>
    <td align="right">39.37</td>
    <td align="right">40.49</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.69</td>
    <td align="right">39.29</td>
    <td align="right">39.61</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.11</td>
    <td align="right">27.45</td>
    <td align="right">27.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.14</td>
    <td align="right">54.78</td>
    <td align="right">54.60</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">30.43</td>
    <td align="right">54.56</td>
    <td align="right">55.10</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.67</td>
    <td align="right">37.07</td>
    <td align="right">27.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.56</td>
    <td align="right">72.75</td>
    <td align="right">72.75</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.24</td>
    <td align="right">84.89</td>
    <td align="right">72.23</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.67</td>
    <td align="right">54.30</td>
    <td align="right">37.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">40.05</td>
    <td align="right">82.41</td>
    <td align="right">82.53</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.87</td>
    <td align="right">87.17</td>
    <td align="right">86.66</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">25.99</td>
    <td align="right">54.64</td>
    <td align="right">37.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.54</td>
    <td align="right">41.32</td>
    <td align="right">42.02</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.32</td>
    <td align="right">42.31</td>
    <td align="right">42.98</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.61</td>
    <td align="right">28.11</td>
    <td align="right">28.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.76</td>
    <td align="right">57.25</td>
    <td align="right">57.05</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.37</td>
    <td align="right">57.88</td>
    <td align="right">57.47</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.92</td>
    <td align="right">37.77</td>
    <td align="right">27.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.13</td>
    <td align="right">76.59</td>
    <td align="right">74.91</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.26</td>
    <td align="right">75.50</td>
    <td align="right">74.97</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.25</td>
    <td align="right">53.55</td>
    <td align="right">36.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.33</td>
    <td align="right">84.96</td>
    <td align="right">86.26</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.26</td>
    <td align="right">98.01</td>
    <td align="right">98.68</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.34</td>
    <td align="right">54.05</td>
    <td align="right">37.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">16.69</td>
    <td align="right">27.62</td>
    <td align="right">27.58</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.66</td>
    <td align="right">29.89</td>
    <td align="right">29.76</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.32</td>
    <td align="right">29.87</td>
    <td align="right">29.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.64</td>
    <td align="right">43.65</td>
    <td align="right">34.31</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.55</td>
    <td align="right">38.70</td>
    <td align="right">28.94</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.11</td>
    <td align="right">46.92</td>
    <td align="right">37.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.17</td>
    <td align="right">53.74</td>
    <td align="right">36.37</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">30.07</td>
    <td align="right">57.75</td>
    <td align="right">39.54</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.87</td>
    <td align="right">57.45</td>
    <td align="right">39.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.26</td>
    <td align="right">62.03</td>
    <td align="right">47.79</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.21</td>
    <td align="right">59.29</td>
    <td align="right">39.93</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">32.05</td>
    <td align="right">78.37</td>
    <td align="right">58.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.95</td>
    <td align="right">27.98</td>
    <td align="right">27.95</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.92</td>
    <td align="right">30.61</td>
    <td align="right">30.29</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.49</td>
    <td align="right">30.82</td>
    <td align="right">30.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.03</td>
    <td align="right">44.51</td>
    <td align="right">34.41</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.88</td>
    <td align="right">38.80</td>
    <td align="right">29.10</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.77</td>
    <td align="right">46.38</td>
    <td align="right">37.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.25</td>
    <td align="right">53.59</td>
    <td align="right">36.81</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.96</td>
    <td align="right">57.80</td>
    <td align="right">39.74</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.80</td>
    <td align="right">57.10</td>
    <td align="right">39.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.30</td>
    <td align="right">54.26</td>
    <td align="right">37.17</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.78</td>
    <td align="right">59.53</td>
    <td align="right">40.16</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.00</td>
    <td align="right">58.91</td>
    <td align="right">39.77</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.48</td>
    <td align="right">33.58</td>
    <td align="right">20.02</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">62.90</td>
    <td align="right">48.41</td>
    <td align="right">35.36</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.13</td>
    <td align="right">24.26</td>
    <td align="right">27.97</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">23.94</td>
    <td align="right">25.39</td>
    <td align="right">26.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">103.08</td>
    <td align="right">104.45</td>
    <td align="right">45.41</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">23.00</td>
    <td align="right">39.15</td>
    <td align="right">41.66</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">34.75</td>
    <td align="right">43.93</td>
    <td align="right">45.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">223.30</td>
    <td align="right">203.68</td>
    <td align="right">61.83</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">36.44</td>
    <td align="right">35.45</td>
    <td align="right">36.69</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">47.29</td>
    <td align="right">46.83</td>
    <td align="right">48.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">347.53</td>
    <td align="right">295.42</td>
    <td align="right">72.54</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">42.99</td>
    <td align="right">42.92</td>
    <td align="right">44.07</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">59.88</td>
    <td align="right">58.53</td>
    <td align="right">60.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.94</td>
    <td align="right">62.50</td>
    <td align="right">41.85</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">22.95</td>
    <td align="right">20.53</td>
    <td align="right">23.65</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">28.62</td>
    <td align="right">27.20</td>
    <td align="right">28.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">157.46</td>
    <td align="right">164.68</td>
    <td align="right">61.77</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.02</td>
    <td align="right">24.07</td>
    <td align="right">25.08</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">34.60</td>
    <td align="right">44.93</td>
    <td align="right">45.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">272.18</td>
    <td align="right">236.31</td>
    <td align="right">66.60</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.01</td>
    <td align="right">37.52</td>
    <td align="right">38.35</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">49.32</td>
    <td align="right">51.05</td>
    <td align="right">49.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">443.13</td>
    <td align="right">359.20</td>
    <td align="right">79.24</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.21</td>
    <td align="right">44.89</td>
    <td align="right">45.55</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.02</td>
    <td align="right">62.32</td>
    <td align="right">62.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.87</td>
    <td align="right">39.43</td>
    <td align="right">40.72</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">27.46</td>
    <td align="right">39.49</td>
    <td align="right">39.80</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.46</td>
    <td align="right">29.62</td>
    <td align="right">29.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.94</td>
    <td align="right">56.23</td>
    <td align="right">56.28</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.53</td>
    <td align="right">57.07</td>
    <td align="right">57.45</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">17.62</td>
    <td align="right">46.33</td>
    <td align="right">35.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">57.25</td>
    <td align="right">86.01</td>
    <td align="right">86.01</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.14</td>
    <td align="right">100.68</td>
    <td align="right">89.11</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">47.24</td>
    <td align="right">79.83</td>
    <td align="right">63.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">74.20</td>
    <td align="right">105.30</td>
    <td align="right">105.43</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.15</td>
    <td align="right">115.61</td>
    <td align="right">115.01</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.95</td>
    <td align="right">92.42</td>
    <td align="right">75.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.03</td>
    <td align="right">51.58</td>
    <td align="right">52.14</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.81</td>
    <td align="right">50.65</td>
    <td align="right">51.43</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.61</td>
    <td align="right">30.32</td>
    <td align="right">30.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">48.10</td>
    <td align="right">76.29</td>
    <td align="right">76.18</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">39.01</td>
    <td align="right">64.53</td>
    <td align="right">64.01</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">20.36</td>
    <td align="right">40.72</td>
    <td align="right">30.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">60.28</td>
    <td align="right">91.04</td>
    <td align="right">89.58</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">65.70</td>
    <td align="right">91.98</td>
    <td align="right">91.61</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">54.25</td>
    <td align="right">83.02</td>
    <td align="right">66.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">74.97</td>
    <td align="right">106.52</td>
    <td align="right">107.66</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.19</td>
    <td align="right">117.58</td>
    <td align="right">117.56</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.87</td>
    <td align="right">90.02</td>
    <td align="right">74.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">17.07</td>
    <td align="right">38.92</td>
    <td align="right">38.75</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">18.85</td>
    <td align="right">31.39</td>
    <td align="right">31.39</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">19.60</td>
    <td align="right">30.99</td>
    <td align="right">30.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.35</td>
    <td align="right">48.26</td>
    <td align="right">39.62</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">20.90</td>
    <td align="right">41.21</td>
    <td align="right">31.52</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">25.62</td>
    <td align="right">51.57</td>
    <td align="right">42.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">47.86</td>
    <td align="right">79.36</td>
    <td align="right">63.64</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">52.44</td>
    <td align="right">82.11</td>
    <td align="right">64.21</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">53.48</td>
    <td align="right">81.72</td>
    <td align="right">63.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">59.13</td>
    <td align="right">90.87</td>
    <td align="right">75.21</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.67</td>
    <td align="right">97.20</td>
    <td align="right">77.94</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">62.83</td>
    <td align="right">97.46</td>
    <td align="right">78.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.35</td>
    <td align="right">30.93</td>
    <td align="right">30.93</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">21.04</td>
    <td align="right">31.96</td>
    <td align="right">31.99</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.75</td>
    <td align="right">33.02</td>
    <td align="right">32.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">23.74</td>
    <td align="right">48.72</td>
    <td align="right">38.89</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">23.66</td>
    <td align="right">40.79</td>
    <td align="right">30.91</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">25.25</td>
    <td align="right">51.41</td>
    <td align="right">42.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.51</td>
    <td align="right">78.98</td>
    <td align="right">61.90</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.16</td>
    <td align="right">82.53</td>
    <td align="right">64.84</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">54.37</td>
    <td align="right">82.33</td>
    <td align="right">64.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.53</td>
    <td align="right">92.18</td>
    <td align="right">75.36</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.14</td>
    <td align="right">97.39</td>
    <td align="right">77.59</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.72</td>
    <td align="right">97.68</td>
    <td align="right">78.05</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
